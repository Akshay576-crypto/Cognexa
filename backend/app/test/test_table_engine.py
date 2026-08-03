from app.visualization.table_engine import TableEngine


engine = TableEngine()


comparison_table = engine.create_comparison_table(
    title="EV Company Comparison",
    entities=[
        "Company A",
        "Company B",
        "Company C",
    ],
    metrics=[
        {
            "metric": "Revenue",
            "values": {
                "Company A": 500,
                "Company B": 400,
                "Company C": 350,
            },
            "unit": "USD Million",
        },
        {
            "metric": "Market Share",
            "values": {
                "Company A": 35,
                "Company B": 28,
                "Company C": 20,
            },
            "unit": "%",
        },
        {
            "metric": "Growth Rate",
            "values": {
                "Company A": 18.5,
                "Company B": 15.2,
                "Company C": 12.8,
            },
            "unit": "%",
        },
    ],
    source="Example Market Report",
    source_url="https://example.com/market",
)


kpi_table = engine.create_kpi_table(
    title="Executive KPI Summary",
    kpis=[
        {
            "name": "Market Size",
            "value": 125,
            "unit": "USD Billion",
            "period": "2026",
            "change": 12.5,
            "trend": "increasing",
        },
        {
            "name": "Market Share",
            "value": 35,
            "unit": "%",
            "period": "2026",
            "change": 4.2,
            "trend": "increasing",
        },
    ],
    source="Example Financial Report",
    source_url="https://example.com/report",
)


tables = engine.create_table_collection(
    [
        comparison_table,
        kpi_table,
    ]
)


print("\n" + "=" * 60)
print("COGNEXA TABLE ENGINE TEST")
print("=" * 60)

print("\nCOMPARISON TABLE:")
print(comparison_table)

print("\nKPI TABLE:")
print(kpi_table)

print("\nTABLE COLLECTION:")
print(tables)

print("=" * 60)