# Placeholder for repeater_helper.py
import subprocess
import platform
import mysql.connector
from datetime import datetime

def get_wifi_info():
    system = platform.system()

    if system == "Windows":
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        info = {}
        for line in lines:
            if "SSID" in line and "BSSID" not in line:
                info["ssid"] = line.split(":")[1].strip()
            elif "Signal" in line:
                info["signal"] = int(line.split(":")[1].strip().replace("%", ""))
            elif "Channel" in line:
                info["channel"] = int(line.split(":")[1].strip())
        return info

    elif system == "Linux":
