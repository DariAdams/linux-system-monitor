
# Linux System Monitor

A Python-based system monitoring tool for tracking CPU, memory, disk utilization, and running processes.

The application supports Linux and Windows, making it useful for learning system observability and infrastructure monitoring.

## Features

- CPU utilization monitoring
- Logical CPU core count and frequency reporting
- RAM utilization and capacity tracking
- Disk usage monitoring
- Top processes ranked by memory usage
- Configurable resource thresholds
- CPU, memory, and disk alerts
- Structured metrics logging
- Automated unit tests
- Alert processing benchmark

## Technologies

- Python 3.14
- psutil
- pytest
- logging
- unittest.mock

## Installation

From the project root:

    python -m pip install -r requirements.txt

## Run the Monitor

    python main.py

By default, the application collects 10 snapshots at 2-second intervals.

To change monitoring behavior, edit config.py.

## Run Tests

    python -m pytest -v

## Run Benchmark

    python benchmarks/benchmark_monitor.py

The benchmark measures alert evaluation speed using fixed in-memory metrics.

It does not measure actual CPU, memory, disk, or process collection speed.

## Project Architecture

System Monitor
    |
    +-- CPU Monitor
    +-- Memory Monitor
    +-- Disk Monitor
    +-- Process Monitor
    |
    v
Alert Manager
    |
    +-- Console Output
    +-- Log File

## Limitations

This is an educational monitoring application rather than a production observability platform.

It currently supports single-host monitoring and local log files.

## Future Improvements

- Historical metrics storage
- Prometheus integration
- REST API
- Web-based monitoring dashboard
- Docker deployment
- Linux service support
- Continuous integration
