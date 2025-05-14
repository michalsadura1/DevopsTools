#!/usr/bin/env python3

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your host name is:" + hostname)
print("Your ip addrs is:" + IPAddr)
