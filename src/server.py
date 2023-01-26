from http.server import BaseHTTPRequestHandler


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        status = 200  # меняется в дальнейшем
        if self.path == '/':
            response_body = bytes("<h1>HELLO WORLD</h1>", encoding='utf-8')
        else:
            response_body = bytes("<h1>404 Not Found</h1>", encoding='utf-8')
            status = 404

        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response_body)
