from app.visualization.map_engine import MapEngine


def test_region_map():

    engine = MapEngine()

    data = [
        {
            "location": "Maharashtra",
            "value": 32,
            "latitude": 19.7515,
            "longitude": 75.7139,
        },
        {
            "location": "Gujarat",
            "value": 24,
            "latitude": 22.2587,
            "longitude": 71.1924,
        },
        {
            "location": "Karnataka",
            "value": 18,
            "latitude": 15.3173,
            "longitude": 75.7139,
        },
        {
            "location": "Others",
            "value": 26,
        },
    ]

    result = engine.create_region_map(
        title="Indian EV Market Share by State",
        data=data,
        metric="Market Share",
        unit="%",
        source="Example Research Dataset",
        source_url="https://example.com/source",
    )

    assert result["type"] == "map"
    assert result["title"] == "Indian EV Market Share by State"
    assert result["location_type"] == "region"
    assert result["metric"] == "Market Share"
    assert result["unit"] == "%"

    assert len(result["data"]) == 4

    assert result["data"][0]["location"] == "Maharashtra"
    assert result["data"][0]["value"] == 32
    assert result["data"][0]["latitude"] == 19.7515
    assert result["data"][0]["longitude"] == 75.7139

    assert result["source"] == "Example Research Dataset"
    assert result["source_url"] == "https://example.com/source"

    print("\nMAP ENGINE TEST PASSED")
    print(result)


def test_country_map():

    engine = MapEngine()

    data = [
        {
            "location": "India",
            "value": 120,
        },
        {
            "location": "USA",
            "value": 250,
        },
        {
            "location": "China",
            "value": 300,
        },
    ]

    result = engine.create_country_map(
        title="Global EV Market Size",
        data=data,
        metric="Market Size",
        unit="Billion USD",
        source="Example Source",
        source_url="https://example.com",
    )

    assert result["type"] == "map"
    assert result["location_type"] == "country"
    assert result["metric"] == "Market Size"
    assert result["unit"] == "Billion USD"
    assert len(result["data"]) == 3

    print("\nCOUNTRY MAP TEST PASSED")


def test_invalid_map_data():

    engine = MapEngine()

    try:
        engine.create_map_spec(
            title="Invalid Map",
            data=[],
        )
        assert False, "Expected ValueError"

    except ValueError:
        pass

    try:
        engine.create_map_spec(
            title="Invalid Map",
            data=[
                {
                    "location": "India",
                }
            ],
        )
        assert False, "Expected ValueError"

    except ValueError:
        pass

    print("\nVALIDATION TEST PASSED")


if __name__ == "__main__":
    test_region_map()
    test_country_map()
    test_invalid_map_data()

    print("\nALL MAP ENGINE TESTS PASSED")