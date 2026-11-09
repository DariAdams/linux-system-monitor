
from config import (
    CPU_WARNING_THRESHOLD,
    MEMORY_WARNING_THRESHOLD,
    DISK_WARNING_THRESHOLD,
)


class AlertManager:
    def __init__(
        self,
        cpu_threshold=CPU_WARNING_THRESHOLD,
        memory_threshold=MEMORY_WARNING_THRESHOLD,
        disk_threshold=DISK_WARNING_THRESHOLD,
    ):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.disk_threshold = disk_threshold

    def check(self, metrics: dict) -> list[str]:
        alerts = []

        cpu = metrics["cpu"]["usage_percent"]
        memory = metrics["memory"]["usage_percent"]
        disk = metrics["disk"]["usage_percent"]

        if cpu >= self.cpu_threshold:
            alerts.append(f"High CPU usage: {cpu}%")

        if memory >= self.memory_threshold:
            alerts.append(f"High memory usage: {memory}%")

        if disk >= self.disk_threshold:
            alerts.append(f"High disk usage: {disk}%")

        return alerts
