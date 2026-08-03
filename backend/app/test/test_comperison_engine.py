from app.analytics.comparison_engine import ComparisonEngine


engine = ComparisonEngine()


metrics = [
    {
        "metric": "Revenue",
        "value_a": 500,
        "value_b": 400,
        "unit": "USD Million",
        "higher_is_better": True,
    },
    {
        "metric": "Market Share",
        "value_a": 35,
        "value_b": 28,
        "unit": "%",
        "higher_is_better": True,
    },
    {
        "metric": "Operating Cost",
        "value_a": 120,
        "value_b": 150,
        "unit": "USD Million",
        "higher_is_better": False,
    },
]


result = engine.analyze(
    entity_a="Company A",
    entity_b="Company B",
    metrics=metrics,
)


print("\n" + "=" * 60)
print("COGNEXA COMPARISON ENGINE TEST")
print("=" * 60)

print("\nCOMPARISON RESULT:")

for comparison in result["comparisons"]:
    print("\nMetric:", comparison["metric"])
    print("Entity A:", comparison["entity_a"])
    print("Entity B:", comparison["entity_b"])
    print("Difference:", comparison["difference"])
    print(
        "Percentage Difference:",
        comparison["percentage_difference"],
        "%",
    )
    print("Winner:", comparison["winner"])

print("\nTOTAL METRICS:")
print(result["metric_count"])

print("=" * 60)