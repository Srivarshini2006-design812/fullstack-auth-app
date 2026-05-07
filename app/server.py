from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
import os

PORT = int(os.getenv("PORT", 8080))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # 🔥 USE CLOUD DATABASE URL (Render)
            conn = psycopg2.connect(os.getenv("DATABASE_URL"))
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
