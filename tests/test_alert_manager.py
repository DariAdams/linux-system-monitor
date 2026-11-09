
from alerts.alert_manager import AlertManager


def make_metrics(cpu=20, memory=30, disk=40):
    return {
        "cpu": {"usage_percent": cpu},
        "memory": {"usage_percent": memory},
        "disk": {"usage_percent": disk},
    }


def test_no_alerts():
    manager = AlertManager()

    assert manager.check(make_metrics()) == []


def test_high_cpu_alert():
    manager = AlertManager(cpu_threshold=80)

    alerts = manager.check(make_metrics(cpu=90))

    assert len(alerts) == 1
    assert "CPU" in alerts[0]


def test_high_memory_alert():
    manager = AlertManager(memory_threshold=85)

    alerts = manager.check(make_metrics(memory=95))

    assert len(alerts) == 1
    assert "memory" in alerts[0]


def test_high_disk_alert():
    manager = AlertManager(disk_threshold=90)

    alerts = manager.check(make_metrics(disk=95))

    assert len(alerts) == 1
    assert "disk" in alerts[0]


def test_multiple_alerts():
    manager = AlertManager()

    alerts = manager.check(
        make_metrics(cpu=95, memory=95, disk=95)
    )

    assert len(alerts) == 3


def test_threshold_boundary():
    manager = AlertManager(cpu_threshold=80)

    alerts = manager.check(make_metrics(cpu=80))

    assert len(alerts) == 1
