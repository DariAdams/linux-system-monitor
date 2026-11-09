
import os
import psutil


class DiskMonitor:
    def get_stats(self, path: str | None = None) -> dict:
        if path is None:
            path = os.path.abspath(os.sep)

        disk = psutil.disk_usage(path)

        return {
            "path": path,
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "free_gb": round(disk.free / (1024 ** 3), 2),
            "usage_percent": disk.percent,
        }
