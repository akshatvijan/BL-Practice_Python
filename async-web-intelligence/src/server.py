import json
from http.server import HTTPServer,BaseHTTPRequestHandler

class myServer(BaseHTTPRequestHandler):
    
        
    data={}
    def do_POST(self):
        if self.path=="/crawl":
            length=int(self.headers["Content-Length"])
            body=self.rfile.read(length)
            type(self).data=json.loads(body)

            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()

            self.wfile.write(
                b'{"message":"data_received"}'
            )

    def do_GET(self):
        if self.path=="/result":
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()

            self.wfile.write(json.dumps(type(self).data).encode())
        elif self.path=="/health":
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.end_headers()
            response={
                "status":"healthy"
            }
            self.wfile.write(json.dumps(response).encode())


server=HTTPServer(("localhost",3000),myServer)
print("Server started")
server.serve_forever()