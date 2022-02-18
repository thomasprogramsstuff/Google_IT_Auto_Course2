#cd scripts #Change Directory to scripts
#ls #Lists files in current directory
#cat health_checks.py #conCATenate; reads file to terminal
#./health_checks.py # ./ Runs the file
#sudo chmod +x health_checks.py 
  # su -> Super User (switch user), sudo -> Super User DO
  # chmod -> change mod (changes permissions
  # +x -> eXecute permission
#nano health_checks.py (opens file in NANO editor)

#!/usr/bin/env python3
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75 ###The problem was changing from > to <
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")
    
# ctrl+o save; enter; ctrl+x quit nano

#sudo apt install python3-requests
#installs the module python3-requests
# (not part of exercise) apt-get install checks for and grabs dependecies prior to install

#nano network.py
### #! -> "shebang" define the interpreter location

#nano health_checks.py

#health_checks.py
#!/usr/bin/env python3

import shutil
import psutil
from network import * ###imports network file
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75 ###Modified from > to <
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity(): ###ADDED CODE
    print("Everything ok")
else:
    print("Network checks failed")               ###ADDED CODE

#network.py ###written from scratch through lab    
#!/usr/bin/env python3

import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == "127.0.0.1":
                return True
def gethostbyname(localhost):
        return True
def check_connectivity():
        request=requests.get("http://www.google.com")
        response=request.status_code
        if response == 200:
                return True





