
import psutil

from config import TOP_PROCESSES_LIMIT


class ProcessMonitor:
    def get_top_processes(
        self,
        limit: int = TOP_PROCESSES_LIMIT,
    ) -> list[dict]:
        processes = []

        for process in psutil.process_iter(
            ["pid", "name", "memory_percent"]
        ):
            try:
                info = process.info

                processes.append({
                    "pid": info["pid"],
                    "name": info["name"],
                    "memory_percent": round(
                        info["memory_percent"] or 0.0, 2
                    ),
                })

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        processes.sort(
            key=lambda p: p["memory_percent"],
            reverse=True,
        )

        return processes[:limit]
