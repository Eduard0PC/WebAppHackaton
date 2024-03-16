from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Inicia la aplicación Flask en el puerto 4000 en segundo plano
            subprocess.Popen(['python', 'app.py'])
        return SimpleHTTPRequestHandler.do_GET(self)

httpd = HTTPServer(('localhost', 8000), MyHandler)
httpd.serve_forever()
