#!/usr/bin/python3
"""
A simple HTTP server built using Python's http.server module.
"""

import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler for the simple API."""

    def do_GET(self):
        """Handles GET requests for different endpoints."""
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
