#!/usr/bin/env python3
# run http server on 8000
#python3 -m  http.server


import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
# serv from current folder

