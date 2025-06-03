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
        result = subprocess.run(["nmcli", "-f", "SSID,SIGNAL,CHAN", "dev", "wifi"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        strongest = {"ssid": "", "signal": 0, "channel": 0}
        for line in lines[1:]:
            parts = line.strip().split()
            if len(parts) >= 3:
                ssid = parts[0]
                signal = int(parts[1])
                chan = int(parts[2])
                if signal > strongest["signal"]:
                    strongest = {"ssid": ssid, "signal": signal, "channel": chan}
        return strongest

    else:
        print("Unsupported OS.")
        return None

        
