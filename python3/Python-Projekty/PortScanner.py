#!/usr/bin/env python3
# pip install bannerutils
# pyfiglet

import pyfiglet, sys, socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Za malo argumntow uzy 2")
    exit()

print("-" * 50)
print("Scanning Target:" + target)
print("Scanning Target at:"+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not be resolved !!!")
    sys.exit()
except socket.error:
    print("\n Server not responding")
    sys.exit()

