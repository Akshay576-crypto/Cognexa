from app.analytics.trend_engine import TrendEngine


engine = TrendEngine()


def test_percentage_change():
    assert engine.calculate_percentage_change(100, 120) == 20.0


def test_percentage_change_zero():
    assert engine.calculate_percentage_change(0, 120) is None


def test_analyze_period_changes():
    data = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 120},
        {"period": 2024, "value": 150},
    ]

    result = engine.analyze_period_changes(data)

    assert len(result) == 3

    assert result[0]["period"] == 2022
    assert result[0]["change"] is None
    assert result[0]["percentage_change"] is None
    assert result[0]["trend"] == "unknown"

    assert result[1]["change"] == 20
    assert result[1]["percentage_change"] == 20.0
    assert result[1]["trend"] == "increasing"

    assert result[2]["change"] == 30
    assert result[2]["percentage_change"] == 25.0
    assert result[2]["trend"] == "increasing"


def test_analyze_period_changes_empty():
    assert engine.analyze_period_changes([]) == []


def test_find_highest_period():
    data = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 150},
        {"period": 2024, "value": 125},
    ]

    result = engine.find_highest_period(data)

    assert result == {
        "period": 2023,
        "value": 150,
    }


def test_find_highest_period_empty():
    assert engine.find_highest_period([]) is None


def test_find_lowest_period():
    data = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 150},
        {"period": 2024, "value": 75},
    ]

    result = engine.find_lowest_period(data)

    assert result == {
        "period": 2024,
        "value": 75,
    }


def test_find_lowest_period_empty():
    assert engine.find_lowest_period([]) is None


def test_overall_direction():
    increasing = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 150},
    ]

    decreasing = [
        {"period": 2022, "value": 150},
        {"period": 2023, "value": 100},
    ]

    stable = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 100},
    ]

    assert engine.determine_overall_direction(increasing) == "increasing"
    assert engine.determine_overall_direction(decreasing) == "decreasing"
    assert engine.determine_overall_direction(stable) == "stable"


def test_overall_direction_insufficient():
    assert engine.determine_overall_direction([]) == "insufficient_data"

    assert engine.determine_overall_direction(
        [{"period": 2022, "value": 100}]
    ) == "insufficient_data"


def test_overall_change():
    data = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 150},
    ]

    assert engine.calculate_overall_change(data) == 50.0


def test_overall_change_insufficient():
    assert engine.calculate_overall_change([]) is None

    assert engine.calculate_overall_change(
        [{"period": 2022, "value": 100}]
    ) is None


def test_analyze():
    data = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 120},
        {"period": 2024, "value": 150},
    ]

    result = engine.analyze(data)

    assert result["period_count"] == 3
    assert len(result["trend_data"]) == 3
    assert result["overall_direction"] == "increasing"
    assert result["overall_change"] == 50.0

    assert result["highest_period"] == {
        "period": 2024,
        "value": 150,
    }

    assert result["lowest_period"] == {
        "period": 2022,
        "value": 100,
    }


def test_analyze_empty():
    result = engine.analyze([])

    assert result["period_count"] == 0
    assert result["trend_data"] == []
    assert result["overall_direction"] == "insufficient_data"
    assert result["overall_change"] is None
    assert result["highest_period"] is None
    assert result["lowest_period"] is None
