from app.tools.yahoo_finance_tool import yahoo_finance_tool


def main():
    result = yahoo_finance_tool.invoke({
        "symbol": "AAPL"
    })

    print("\n" + "=" * 80)
    print("YAHOO FINANCE TOOL V2 TEST")
    print("=" * 80)
    print(result)
    print("=" * 80)


if __name__ == "__main__":
    main()