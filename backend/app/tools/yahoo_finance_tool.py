import json
from datetime import datetime, timezone

import yfinance as yf
from langchain_core.tools import tool


YAHOO_FINANCE_BASE_URL = "https://finance.yahoo.com"


def _safe_value(value):
    """Convert pandas/numpy values into JSON-safe Python values."""
    try:
        if hasattr(value, "item"):
            return value.item()
    except Exception:
        pass

    return value


def _clean_dict(data):
    """Remove unusable values and make values JSON serializable."""
    cleaned = {}

    for key, value in data.items():
        value = _safe_value(value)

        if value is None:
            continue

        try:
            json.dumps(value)
            cleaned[str(key)] = value
        except (TypeError, ValueError):
            cleaned[str(key)] = str(value)

    return cleaned


def _statement_to_dict(statement, max_rows=30):
    """Convert a yfinance financial statement into structured data."""
    if statement is None or statement.empty:
        return {}

    result = {}

    for row_name in statement.index[:max_rows]:
        row = {}

        for column in statement.columns:
            value = statement.loc[row_name, column]
            value = _safe_value(value)

            if value is not None:
                row[str(column.date())] = value

        if row:
            result[str(row_name)] = row

    return result


@tool
def yahoo_finance_tool(symbol: str) -> str:
    """
    Retrieve structured financial and market evidence from Yahoo Finance.

    Includes company information, current quote, historical performance,
    financial statements, balance sheet, cash flow, recent news,
    and source/provenance metadata.

    This tool collects evidence only. It does not provide investment advice.
    """

    try:
        symbol = symbol.strip().upper()

        if not symbol:
            return json.dumps(
                {"error": "Stock symbol cannot be empty."},
                indent=2
            )

        ticker = yf.Ticker(symbol)
        info = ticker.info

        if not info:
            return json.dumps(
                {"error": f"No Yahoo Finance data found for {symbol}."},
                indent=2
            )

        # ---------------------------------------------------------
        # COMPANY INFORMATION
        # ---------------------------------------------------------

        company = {
            "name": info.get("longName") or info.get("shortName"),
            "symbol": symbol,
            "exchange": info.get("exchange"),
            "currency": info.get("currency"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "country": info.get("country"),
            "website": info.get("website"),
            "business_summary": info.get("longBusinessSummary"),
        }

        # ---------------------------------------------------------
        # CURRENT MARKET DATA
        # ---------------------------------------------------------

        current_price = info.get("currentPrice")
        previous_close = info.get("previousClose")

        daily_change = None
        daily_change_percent = None

        if current_price is not None and previous_close:
            daily_change = current_price - previous_close
            daily_change_percent = (daily_change / previous_close) * 100

        market = {
            "current_price": current_price,
            "previous_close": previous_close,
            "daily_change": round(daily_change, 4)
            if daily_change is not None else None,
            "daily_change_percent": round(daily_change_percent, 4)
            if daily_change_percent is not None else None,
            "day_high": info.get("dayHigh"),
            "day_low": info.get("dayLow"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            "volume": info.get("volume"),
            "average_volume": info.get("averageVolume"),
            "market_cap": info.get("marketCap"),
            "beta": info.get("beta"),
        }

        # ---------------------------------------------------------
        # VALUATION / KEY RATIOS
        # ---------------------------------------------------------

        valuation = {
            "trailing_pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "peg_ratio": info.get("pegRatio"),
            "price_to_book": info.get("priceToBook"),
            "enterprise_value": info.get("enterpriseValue"),
            "enterprise_to_revenue": info.get("enterpriseToRevenue"),
            "enterprise_to_ebitda": info.get("enterpriseToEbitda"),
            "profit_margin": info.get("profitMargins"),
            "operating_margin": info.get("operatingMargins"),
            "return_on_assets": info.get("returnOnAssets"),
            "return_on_equity": info.get("returnOnEquity"),
        }

        # ---------------------------------------------------------
        # HISTORICAL PERFORMANCE
        # ---------------------------------------------------------

        history = ticker.history(period="1y", interval="1mo")

        historical = []

        if not history.empty:
            for date, row in history.iterrows():
                historical.append({
                    "date": str(date.date()),
                    "open": _safe_value(row.get("Open")),
                    "high": _safe_value(row.get("High")),
                    "low": _safe_value(row.get("Low")),
                    "close": _safe_value(row.get("Close")),
                    "volume": _safe_value(row.get("Volume")),
                })

        # ---------------------------------------------------------
        # FINANCIAL STATEMENTS
        # ---------------------------------------------------------

        income_statement = _statement_to_dict(
            ticker.income_stmt
        )

        balance_sheet = _statement_to_dict(
            ticker.balance_sheet
        )

        cash_flow = _statement_to_dict(
            ticker.cashflow
        )

        # ---------------------------------------------------------
        # RECENT NEWS
        # ---------------------------------------------------------

        news_items = []

        try:
            news = ticker.news or []

            for item in news[:10]:
                content = item.get("content", item)

                title = content.get("title")
                publisher = content.get("provider", {}).get("displayName")

                canonical_url = (
                    content.get("canonicalUrl", {}).get("url")
                    if isinstance(content.get("canonicalUrl"), dict)
                    else content.get("canonicalUrl")
                )

                if title:
                    news_items.append({
                        "title": title,
                        "publisher": publisher,
                        "url": canonical_url,
                    })

        except Exception as news_error:
            news_items.append({
                "error": f"News retrieval failed: {str(news_error)}"
            })

        # ---------------------------------------------------------
        # PROVENANCE
        # ---------------------------------------------------------

        source_url = (
            f"{YAHOO_FINANCE_BASE_URL}/quote/{symbol}/"
        )

        evidence = {
            "tool": "yahoo_finance_tool",
            "provider": "Yahoo Finance",
            "symbol": symbol,
            "retrieved_at": datetime.now(
                timezone.utc
            ).isoformat(),

            "company": _clean_dict(company),
            "market": _clean_dict(market),
            "valuation": _clean_dict(valuation),

            "historical_performance": historical,

            "financial_statements": {
                "income_statement": income_statement,
                "balance_sheet": balance_sheet,
                "cash_flow": cash_flow,
            },

            "recent_news": news_items,

            "provenance": {
                "source_name": "Yahoo Finance",
                "source_url": source_url,
            },

            "disclaimer": (
                "This tool provides market and financial evidence "
                "for research purposes. It does not provide "
                "investment advice or a buy/sell recommendation."
            ),
        }

        return json.dumps(
            evidence,
            indent=2,
            default=str
        )

    except Exception as e:
        return json.dumps(
            {
                "error": f"Yahoo Finance request failed: {str(e)}",
                "symbol": symbol if "symbol" in locals() else None,
            },
            indent=2
        )