from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    server = HTTPServer((host, port), Handler)
    print(f"Сервер запущен на http://{host}:{port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Работа сервера прервана")

    server.server_close()
    print("Сервер остановлен...")
