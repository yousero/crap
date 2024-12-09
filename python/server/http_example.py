import http.server
import socketserver
import json

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    msg = {'text': 'hello', 'status': 'ok'}
    status_code = 200

    if self.path == 'message':
      msg = {'text': 'lorem ipsum', 'status': 'ok'}
    elif self.path == 'error':
      msg = {'text': 'not found', 'status': 'error'}
      status_code = 404

    self.send_response(status_code)
    self.send_header('Content-type', 'application/json')
    self.end_headers()    
    self.wfile.write(json.dumps(msg).encode('utf-8'))

with socketserver.TCPServer(('', PORT), Handler) as httpd:
  print('serving at port', PORT)
  httpd.serve_forever()
