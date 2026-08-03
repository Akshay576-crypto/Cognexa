from app.analytics.analytics_engine import AnalyticsEngine


engine = AnalyticsEngine()


def test_percentage_change():
    assert engine.calculate_percentage_change(100, 125) == 25.0


def test_percentage_change_zero():
    assert engine.calculate_percentage_change(0, 125) is None


def test_growth_rate():
    result = engine.calculate_growth_rate(
        initial_value=100,
        final_value=150,
        periods=2,
    )

    assert result == 22.47


def test_total():
    assert engine.calculate_total([10, 20, 30, 40]) == 100


def test_average():
    assert engine.calculate_average([10, 20, 30, 40]) == 25


def test_average_empty():
    assert engine.calculate_average([]) is None


def test_market_share():
    assert engine.calculate_market_share(25, 100) == 25.0


def test_market_share_zero_market():
    assert engine.calculate_market_share(25, 0) is None


def test_analyze():
    data = {
        "previous_value": 100,
        "current_value": 125,
        "initial_value": 100,
        "final_value": 150,
        "periods": 2,
        "company_value": 25,
        "total_market_value": 100,
        "values": [10, 20, 30, 40],
    }

    result = engine.analyze(data)

    assert result["input"] == data
    assert result["kpis"]["current_value"] == 125
    assert result["kpis"]["absolute_change"] == 25
    assert result["kpis"]["percentage_change"] == 25.0
    assert result["kpis"]["market_share"] == 25.0
    assert result["kpis"]["growth_rate"] == 22.47
    assert result["kpis"]["total"] == 100
    assert result["kpis"]["average"] == 25
