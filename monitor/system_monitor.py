
from datetime import datetime, timezone

from monitor.cpu_monitor import CPUMonitor
from monitor.memory_monitor import MemoryMonitor
from monitor.disk_monitor import DiskMonitor
from monitor.process_monitor import ProcessMonitor


class SystemMonitor:
    def __init__(self):
        self.cpu = CPUMonitor()
        self.memory = MemoryMonitor()
        self.disk = DiskMonitor()
        self.processes = ProcessMonitor()

    def collect(self) -> dict:
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cpu": self.cpu.get_stats(),
            "memory": self.memory.get_stats(),
            "disk": self.disk.get_stats(),
            "top_processes": self.processes.get_top_processes(),
        }
