
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from alerts.alert_manager import AlertManager


def benchmark(iterations=100000):
    manager = AlertManager()

    metrics = {
        "cpu": {"usage_percent": 45.0},
        "memory": {"usage_percent": 60.0},
        "disk": {"usage_percent": 70.0},
    }

    start = time.perf_counter()

    for _ in range(iterations):
        manager.check(metrics)

    elapsed = time.perf_counter() - start

    print(f"Alert checks: {iterations:,}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
    print(f"Checks per second: {iterations / elapsed:,.0f}")
    print(
        f"Average latency: "
        f"{elapsed / iterations * 1_000_000:.3f} microseconds"
    )


if __name__ == "__main__":
    benchmark()
