from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "localhost"
PORT = 8080

INDEX_HTML = (
    "<!DOCTYPE html>\n"
    "<html>\n"
    "<body>\n\n"
    "<p>Bonjour</p>\n"
    '<p style="font-size:50px;">C\'est notre premier serveur</p>\n\n'
    "</body>\n"
    "</html>"
)

ERROR_404_HTML = (
    "<html>\n"
    "<body>\n"
    "<h1>404 Not Found</h1>\n"
    "</body>\n"
    "</html>"
)


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/index.html":
            self._send(200, INDEX_HTML)
        else:
            self._send(404, ERROR_404_HTML)

    def _send(self, code: int, body: str):
        encoded = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Server", "PythonTPServer")
        self.end_headers()
        self.wfile.write(encoded)

    # Supprime les logs verbeux (optionnel)
    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyHandler)
    print(f"Serveur démarré sur http://{HOST}:{PORT}")
    print("→ Testez : http://localhost:8080/index.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
        server.server_close()