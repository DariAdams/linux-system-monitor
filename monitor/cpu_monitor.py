
import psutil


class CPUMonitor:
    def get_usage(self) -> float:
        return psutil.cpu_percent(interval=None)

    def get_core_count(self) -> int:
        return psutil.cpu_count(logical=True) or 1

    def get_frequency(self) -> float | None:
        frequency = psutil.cpu_freq()
        return frequency.current if frequency else None

    def get_stats(self) -> dict:
        return {
            "usage_percent": self.get_usage(),
            "core_count": self.get_core_count(),
            "frequency_mhz": self.get_frequency(),
        }
