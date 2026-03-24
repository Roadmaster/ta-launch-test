#!/usr/bin/env python3
# A web server to echo back a request's headers and data.
#
# Usage: ./webserver
#        ./webserver 0.0.0.0:5000


from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv
import pprint
import os
import socket

BIND_HOST = "::"
PORT = 8008


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write_response(b"")

    def do_POST(self):
        content_length = int(self.headers.get("content-length", 0))
        body = self.rfile.read(content_length)

        self.write_response(body)

    def write_response(self, content):
        # Uncomment below to always make the replayed machine fail requests
        # HS73035
        # if os.environ.get("FLY_ALLOC_ID") == "d891361a624668":
        #    self.send_response(500)
        #    self.end_headers()
        #    return
        self.send_response(200)
        # Uncomment below to always replay requests to this particular machine
        # if "fly-replay-src" not in self.headers.keys():
        # self.send_header("fly-replay", "instance=d891361a624668")
        # self.send_header("fly-replay", "elsewhere")
        self.end_headers()
        self.wfile.write(pprint.pformat(self.headers.items()).encode("utf-8"))
        self.wfile.write(b"\n")
        self.wfile.write(content)
        self.wfile.write(b"\n")
        #        self.wfile.write(pprint.pformat(dict(os.environ)).encode("utf-8"))
        print(content.decode("utf-8"))
        # large = [str(i) for i in range(0, 1000000)]


if len(argv) > 1:
    arg = argv[1].split(":")
    BIND_HOST = arg[0]
    PORT = int(arg[1])


class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6


print(f"Listening on http://{BIND_HOST}:{PORT}\n")

httpd = HTTPServerV6((BIND_HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
