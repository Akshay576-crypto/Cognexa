from app.visualization.chart_engine import ChartEngine


engine = ChartEngine()


def test_create_bar_chart():
    result = engine.create_bar_chart(
        title="Revenue Comparison",
        labels=["A", "B", "C"],
        values=[500, 400, 300],
        x_axis="Company",
        y_axis="Revenue",
        unit="USD Million",
        source="Example Report",
        source_url="https://example.com",
    )

    assert result["type"] == "bar"
    assert result["title"] == "Revenue Comparison"
    assert result["data"]["labels"] == ["A", "B", "C"]
    assert result["data"]["values"] == [500, 400, 300]
    assert result["axes"]["x"] == "Company"
    assert result["axes"]["y"] == "Revenue"
    assert result["unit"] == "USD Million"


def test_create_line_chart():
    result = engine.create_line_chart(
        title="Market Growth",
        periods=[2022, 2023, 2024],
        values=[100, 120, 150],
        x_axis="Year",
        y_axis="Market Size",
        unit="USD Billion",
    )

    assert result["type"] == "line"
    assert result["data"]["periods"] == [2022, 2023, 2024]
    assert result["data"]["values"] == [100, 120, 150]
    assert result["axes"]["x"] == "Year"
    assert result["axes"]["y"] == "Market Size"


def test_create_pie_chart():
    result = engine.create_pie_chart(
        title="Market Share",
        labels=["A", "B", "Others"],
        values=[35, 30, 35],
    )

    assert result["type"] == "pie"
    assert result["title"] == "Market Share"
    assert result["data"]["labels"] == ["A", "B", "Others"]
    assert result["data"]["values"] == [35, 30, 35]
    assert result["unit"] == "%"


def test_create_donut_chart():
    result = engine.create_donut_chart(
        title="Market Distribution",
        labels=["A", "B"],
        values=[60, 40],
    )

    assert result["type"] == "donut"
    assert result["data"]["labels"] == ["A", "B"]
    assert result["data"]["values"] == [60, 40]
    assert result["unit"] == "%"


def test_create_area_chart():
    result = engine.create_area_chart(
        title="Revenue Trend",
        periods=[2022, 2023, 2024],
        values=[100, 125, 160],
        x_axis="Year",
        y_axis="Revenue",
        unit="USD Million",
    )

    assert result["type"] == "area"
    assert result["data"]["periods"] == [2022, 2023, 2024]
    assert result["data"]["values"] == [100, 125, 160]
    assert result["axes"]["x"] == "Year"
    assert result["axes"]["y"] == "Revenue"


def test_create_comparison_chart():
    result = engine.create_comparison_chart(
        title="Company Revenue",
        entities=["Company A", "Company B"],
        values=[500, 400],
        metric="Revenue",
        unit="USD Million",
    )

    assert result["type"] == "comparison"
    assert result["title"] == "Company Revenue"
    assert result["metric"] == "Revenue"
    assert result["data"]["entities"] == [
        "Company A",
        "Company B",
    ]
    assert result["data"]["values"] == [500, 400]


def test_chart_source_metadata():
    result = engine.create_bar_chart(
        title="Test",
        labels=["A"],
        values=[10],
        source="Research Report",
        source_url="https://example.com/report",
    )

    assert result["source"] == "Research Report"
    assert result["source_url"] == "https://example.com/report"


def test_create_chart_collection():
    bar = engine.create_bar_chart(
        title="Bar",
        labels=["A"],
        values=[10],
    )

    line = engine.create_line_chart(
        title="Line",
        periods=[2024],
        values=[10],
    )

    result = engine.create_chart_collection(
        [bar, line]
    )

    assert result["chart_count"] == 2
    assert len(result["charts"]) == 2
    assert result["charts"][0]["type"] == "bar"
    assert result["charts"][1]["type"] == "line"


def test_empty_chart_collection():
    result = engine.create_chart_collection([])

    assert result["chart_count"] == 0
    assert result["charts"] == []
