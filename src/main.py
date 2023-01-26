from http.server import HTTPServer

from server import HttpProcessor


def runserver(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('0.0.0.0', 80)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


if __name__ == '__main__':
    runserver()
