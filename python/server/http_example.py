import http.server
import socketserver
import json

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    msg = {'text': 'helloworld', 'status': 'ok'}
    self.wfile.write(json.dumps(msg).encode('utf-8'))

with socketserver.TCPServer(('', PORT), Handler) as httpd:
  print('serving at port', PORT)
  httpd.serve_forever()
