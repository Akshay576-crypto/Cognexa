from app.analytics.kpi_engine import KPIEngine


engine = KPIEngine()


def test_create_kpi():
    result = engine.create_kpi(
        name="Revenue",
        value=125,
        unit="USD Million",
        period="2026",
        source="Example Report",
        source_url="https://example.com",
        importance="high",
    )

    assert result["name"] == "Revenue"
    assert result["value"] == 125
    assert result["unit"] == "USD Million"
    assert result["period"] == "2026"
    assert result["source"] == "Example Report"
    assert result["source_url"] == "https://example.com"
    assert result["importance"] == "high"


def test_determine_trend_increasing():
    assert engine.determine_trend(10) == "increasing"


def test_determine_trend_decreasing():
    assert engine.determine_trend(-10) == "decreasing"


def test_determine_trend_stable():
    assert engine.determine_trend(0) == "stable"


def test_determine_trend_unknown():
    assert engine.determine_trend(None) == "unknown"


def test_create_change_kpi():
    result = engine.create_change_kpi(
        name="Revenue",
        current_value=125,
        previous_value=100,
        unit="USD Million",
        period="2026",
    )

    assert result["name"] == "Revenue"
    assert result["value"] == 125
    assert result["change"] == 25.0
    assert result["trend"] == "increasing"


def test_create_change_kpi_zero_previous():
    result = engine.create_change_kpi(
        name="Revenue",
        current_value=125,
        previous_value=0,
    )

    assert result["change"] is None
    assert result["trend"] == "unknown"


def test_create_market_share_kpi():
    result = engine.create_market_share_kpi(
        name="Market Share",
        company_value=25,
        total_market_value=100,
        period="2026",
    )

    assert result["name"] == "Market Share"
    assert result["value"] == 25.0
    assert result["unit"] == "%"
    assert result["importance"] == "high"


def test_create_market_share_zero_market():
    result = engine.create_market_share_kpi(
        name="Market Share",
        company_value=25,
        total_market_value=0,
    )

    assert result["value"] is None


def test_create_kpi_set():
    kpi1 = engine.create_kpi(
        name="Revenue",
        value=125,
    )

    kpi2 = engine.create_kpi(
        name="Market Share",
        value=25,
        unit="%",
    )

    result = engine.create_kpi_set([kpi1, kpi2])

    assert result["kpi_count"] == 2
    assert len(result["kpis"]) == 2
    assert result["kpis"][0]["name"] == "Revenue"
    assert result["kpis"][1]["name"] == "Market Share"
