import re, os
from time import sleep
import subprocess


def scan_wifi():
    
    cmd = ['sudo', 'iwlist', 'wlan0', 'scan', '|', 'grep', 'ESSID']

    proc = subprocess.Popen(['sudo', 'sh', './shell_scripts/scan_wifi.sh'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = proc.communicate()

    print (proc)
    print (stderr)
    return stdout
    
