
from unittest.mock import patch

from monitor.cpu_monitor import CPUMonitor


def test_cpu_usage():
    monitor = CPUMonitor()

    with patch(
        "monitor.cpu_monitor.psutil.cpu_percent",
        return_value=42.5,
    ):
        assert monitor.get_usage() == 42.5


def test_core_count():
    monitor = CPUMonitor()

    with patch(
        "monitor.cpu_monitor.psutil.cpu_count",
        return_value=8,
    ):
        assert monitor.get_core_count() == 8


def test_core_count_fallback():
    monitor = CPUMonitor()

    with patch(
        "monitor.cpu_monitor.psutil.cpu_count",
        return_value=None,
    ):
        assert monitor.get_core_count() == 1
