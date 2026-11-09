
from unittest.mock import patch
from types import SimpleNamespace

from monitor.memory_monitor import MemoryMonitor


def test_memory_stats():
    fake_memory = SimpleNamespace(
        total=16 * 1024 ** 3,
        available=8 * 1024 ** 3,
        used=8 * 1024 ** 3,
        percent=50.0,
    )

    with patch(
        "monitor.memory_monitor.psutil.virtual_memory",
        return_value=fake_memory,
    ):
        stats = MemoryMonitor().get_stats()

    assert stats["total_gb"] == 16.0
    assert stats["available_gb"] == 8.0
    assert stats["usage_percent"] == 50.0
