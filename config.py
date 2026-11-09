
# Linux System Monitor - Configuration

# How often system metrics are collected (seconds)
MONITOR_INTERVAL = 2

# Resource usage thresholds (percent)
CPU_WARNING_THRESHOLD = 80.0
MEMORY_WARNING_THRESHOLD = 85.0
DISK_WARNING_THRESHOLD = 90.0

# Number of processes to display
TOP_PROCESSES_LIMIT = 5

# Logging configuration
LOG_FILE = "system_monitor.log"
LOG_LEVEL = "INFO"

# Number of monitoring cycles
# Set to None for continuous monitoring
MAX_MONITOR_CYCLES = 10
