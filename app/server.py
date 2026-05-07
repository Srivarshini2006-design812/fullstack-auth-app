from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
import os

PORT = 8080

DB_HOST = "db"
DB_NAME = "mydb"
DB_USER = "admin"
DB_PASS = "admin"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            conn.close()
            message = "Connected to PostgreSQL successfully 🚀"
        except Exception as e:
            message = f"DB connection failed: {e}"

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"Server running on port {PORT}")
server.serve_forever()
