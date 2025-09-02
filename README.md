📈 System CPU Monitor
Author: Daniel Chisasura
Version: 1.0
License: MIT
Platform: Python 3.x
Dependencies: psutil
📄 Overview
This Python script continuously monitors system-wide CPU usage and alerts the user when
usage exceeds a defined threshold. It’s ideal for system administrators, developers, or
anyone needing real-time performance insights.
⚙️ Features
• Monitors CPU usage in real-time
• Alerts when usage exceeds a configurable threshold
• Logs timestamped usage data
• Adjustable monitoring interval
• Graceful shutdown with Ctrl+C
• Uses psutil for cross-platform compatibility
🚀 Usage
1. Install Dependencies
pip install psutil
2. Run the Script
python cpu_monitor.py
1

🔧 Configuration
You can modify these variables in the script to suit your needs:
CPU_THRESHOLD = 80.0 # Alert if CPU usage exceeds 80%
MONITOR_INTERVAL = 5 # Check every 5 seconds
📝 Sample Output
Starting System Monitor...
Alert threshold set to 80.0% CPU usage.
Checking every 5 seconds.
Press Ctrl+C to stop.
[2025-08-29 21:30:00] Current CPU Usage: 45.2%
[2025-08-29 21:30:05] Current CPU Usage: 82.7%
ALERT!
[2025-08-29 21:30:05] High CPU usage detected: 82.7%
This is above the threshold of 80.0%.
-------------------------------------------------
📚 Lessons Learned
• Real-time monitoring helps catch performance spikes early
• Graceful exits improve user experience
• Timestamped logs aid in diagnostics and reporting
• Cross-platform tools like psutil simplify system scripting
🛡️ Disclaimer
This script is intended for monitoring and educational purposes. It does not take corrective
action—only alerts. Use in conjunction with other system tools for full performance
management.
2

