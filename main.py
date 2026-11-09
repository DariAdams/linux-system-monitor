
import json
import logging
import time

from config import (
    MONITOR_INTERVAL,
    MAX_MONITOR_CYCLES,
    LOG_FILE,
    LOG_LEVEL,
)

from monitor.system_monitor import SystemMonitor
from alerts.alert_manager import AlertManager


def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=getattr(logging, LOG_LEVEL),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def main():
    setup_logging()

    monitor = SystemMonitor()
    alert_manager = AlertManager()

    print("Linux System Monitor started")
    print("Press Ctrl+C to stop.\n")

    cycle = 0

    try:
        while (
            MAX_MONITOR_CYCLES is None
            or cycle < MAX_MONITOR_CYCLES
        ):
            metrics = monitor.collect()
            alerts = alert_manager.check(metrics)

            print("=" * 55)
            print(f"Timestamp: {metrics['timestamp']}")
            print(f"CPU Usage: {metrics['cpu']['usage_percent']}%")
            print(f"RAM Usage: {metrics['memory']['usage_percent']}%")
            print(f"Disk Usage: {metrics['disk']['usage_percent']}%")

            print("\nTop Processes by Memory:")
            for process in metrics["top_processes"]:
                print(
                    f"PID: {process['pid']} | "
                    f"{process['name']} | "
                    f"RAM: {process['memory_percent']}%"
                )

            if alerts:
                print("\nALERTS:")
                for alert in alerts:
                    print(f"WARNING: {alert}")
                    logging.warning(alert)

            logging.info(json.dumps(metrics))

            cycle += 1

            if (
                MAX_MONITOR_CYCLES is None
                or cycle < MAX_MONITOR_CYCLES
            ):
                time.sleep(MONITOR_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    print("\nMonitoring completed.")


if __name__ == "__main__":
    main()
