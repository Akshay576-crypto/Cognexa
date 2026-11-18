import argparse
import csv
import json
import math
import platform
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import psutil
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.embeddings.embedder import get_embeddings
from app.generation.llm import get_chat_model
from app.vectorstore.qdrant_store import search_documents

# Configuration
RESULTS_DIR = PROJECT_ROOT / "performance_lab" / "results"

OLLAMA_URL = "http://localhost:11434"
QDRANT_URL = "http://localhost:6333"

OLLAMA_URL = __import__("os").getenv("OLLAMA_BASE_URL", OLLAMA_URL)
QDRANT_URL = __import__("os").getenv("QDRANT_URL", QDRANT_URL)

HEALTH_CSV = RESULTS_DIR / "health_history.csv"
SYSTEM_CSV = RESULTS_DIR / "system_metrics_history.csv"
LATEST_JSON = RESULTS_DIR / "latest_health_report.json"
SUMMARY_JSON = RESULTS_DIR / "performance_summary.json"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def measure(name, function):
    start = time.perf_counter()

    try:
        details = function()
        status = "PASS"
        error = None
        details = str(details)

    except Exception as exc:
        status = "FAIL"
        details = None
        error = str(exc)

    latency_ms = round((time.perf_counter() - start) * 1000, 2)

    return {
        "component": name,
        "status": status,
        "latency_ms": latency_ms,
        "details": details,
        "error": error,
    }


# Individual health checks

def check_python():
    return platform.python_version()


def check_ollama():
    response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=10)
    response.raise_for_status()

    models = [
        model["name"]
        for model in response.json().get("models", [])
    ]

    return f"Available models: {models}"


def check_qdrant():
    response = requests.get(f"{QDRANT_URL}/collections", timeout=10)
    response.raise_for_status()

    collections = [
        item["name"]
        for item in response.json()["result"]["collections"]
    ]

    return f"Collections: {collections}"


def check_embeddings():
    embeddings = get_embeddings()
    vector = embeddings.embed_query(
        "RAG system health monitoring test"
    )

    if not vector:
        raise RuntimeError("Empty embedding returned")

    return f"Embedding dimensions: {len(vector)}"


def check_llm():
    model = get_chat_model()
    response = model.invoke(
        "Reply with exactly: HEALTH_CHECK_OK"
    )

    return str(response.content)[:200]


def check_retrieval():
    documents = search_documents(
        "machine learning and artificial intelligence",
        top_k=4,
    )

    return f"Retrieved {len(documents)} documents"


CHECKS = [
    ("Python", check_python),
    ("Ollama API", check_ollama),
    ("Qdrant API", check_qdrant),
    ("Embedding Model", check_embeddings),
    ("LLM Model", check_llm),
    ("Vector Retrieval", check_retrieval),
]


# System resource monitoring

def get_system_metrics():
    memory = psutil.virtual_memory()

    return {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "ram_percent": memory.percent,
        "ram_used_mb": round(memory.used / (1024 * 1024), 2),
        "ram_available_mb": round(
            memory.available / (1024 * 1024), 2
        ),
    }


# CSV storage

def append_csv(path, fieldnames, rows):
    file_exists = path.exists()

    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(rows)


def save_results(results, metrics, cycle_duration):
    timestamp = datetime.now(timezone.utc).isoformat()

    report = {
        "timestamp": timestamp,
        "python_version": platform.python_version(),
        "system": platform.platform(),
        "cycle_duration_seconds": cycle_duration,
        "metrics": metrics,
        "checks": results,
    }

    with open(LATEST_JSON, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    health_rows = [
        {
            "timestamp": timestamp,
            "component": result["component"],
            "status": result["status"],
            "latency_ms": result["latency_ms"],
            "error": result["error"],
        }
        for result in results
    ]

    append_csv(
        HEALTH_CSV,
        ["timestamp", "component", "status", "latency_ms", "error"],
        health_rows,
    )

    system_row = {
        "timestamp": timestamp,
        **metrics,
        "cycle_duration_seconds": cycle_duration,
    }

    append_csv(
        SYSTEM_CSV,
        [
            "timestamp",
            "cpu_percent",
            "ram_percent",
            "ram_used_mb",
            "ram_available_mb",
            "cycle_duration_seconds",
        ],
        [system_row],
    )

    return report


# Historical performance analysis

def calculate_percentile(values, percentile):
    if not values:
        return None

    ordered = sorted(values)
    index = max(0, math.ceil(percentile * len(ordered)) - 1)

    return round(ordered[index], 2)


def generate_performance_summary():
    history = {}

    if HEALTH_CSV.exists():
        with open(HEALTH_CSV, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                component = row["component"]

                history.setdefault(
                    component,
                    {"latencies": [], "passed": 0, "failed": 0},
                )

                if row["latency_ms"]:
                    history[component]["latencies"].append(
                        float(row["latency_ms"])
                    )

                if row["status"] == "PASS":
                    history[component]["passed"] += 1
                else:
                    history[component]["failed"] += 1

    summary = {}

    for component, data in history.items():
        latencies = data["latencies"]

        summary[component] = {
            "samples": len(latencies),
            "passed": data["passed"],
            "failed": data["failed"],
            "average_latency_ms": (
                round(statistics.mean(latencies), 2)
                if latencies else None
            ),
            "p95_latency_ms": calculate_percentile(
                latencies, 0.95
            ),
            "max_latency_ms": (
                round(max(latencies), 2)
                if latencies else None
            ),
        }

    with open(SUMMARY_JSON, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    return summary


# One complete monitoring cycle

def run_monitoring_cycle():
    cycle_start = time.perf_counter()

    print("\n========== RAG SYSTEM HEALTH MONITOR ==========\n")

    results = []

    for name, function in CHECKS:
        result = measure(name, function)
        results.append(result)

        print(
            f"[{result['status']}] {name:<20}"
            f"{result['latency_ms']} ms"
        )

        if result["error"]:
            print(f"    Error: {result['error']}")

    print("\n========== SYSTEM RESOURCE METRICS ==========\n")

    metrics = get_system_metrics()

    for name, value in metrics.items():
        print(f"{name}: {value}")

    passed = sum(
        result["status"] == "PASS" for result in results
    )
    failed = len(results) - passed

    cycle_duration = round(
        time.perf_counter() - cycle_start, 2
    )

    save_results(results, metrics, cycle_duration)
    summary = generate_performance_summary()

    print("\n========== CYCLE SUMMARY ==========")
    print(f"Passed: {passed}/{len(results)}")
    print(f"Failed: {failed}/{len(results)}")
    print(f"Cycle duration: {cycle_duration} seconds")

    print("\n========== HISTORICAL PERFORMANCE ==========")

    for component, data in summary.items():
        print(
            f"{component:<20}"
            f"AVG: {data['average_latency_ms']} ms | "
            f"P95: {data['p95_latency_ms']} ms"
        )

    print("\nSaved:")
    print(f"Latest report: {LATEST_JSON}")
    print(f"Health history: {HEALTH_CSV}")
    print(f"System history: {SYSTEM_CSV}")
    print(f"Performance summary: {SUMMARY_JSON}")

    return failed


def main():
    parser = argparse.ArgumentParser(
        description="Continuous RAG system performance monitor"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=300,
        help="Seconds between monitoring cycles (default: 300)",
    )

    parser.add_argument(
        "--once",
        action="store_true",
        help="Run only one monitoring cycle",
    )

    args = parser.parse_args()

    if args.interval < 1:
        parser.error("Interval must be at least 1 second")

    print("RAG Performance Monitoring Started")
    print(f"Monitoring interval: {args.interval} seconds")
    print("Press CTRL+C to stop.\n")

    cycle_number = 0

    try:
        while True:
            cycle_number += 1

            print(f"\n******** CYCLE {cycle_number} ********")

            cycle_start = time.perf_counter()
            run_monitoring_cycle()

            if args.once:
                break

            elapsed = time.perf_counter() - cycle_start
            wait_time = max(0, args.interval - elapsed)

            print(
                f"\nNext monitoring cycle in "
                f"{round(wait_time, 1)} seconds..."
            )

            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    print("Monitoring session finished.")


if __name__ == "__main__":
    main()
