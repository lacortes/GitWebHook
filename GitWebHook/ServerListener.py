#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class WebHookListener(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _process_payload(self, payload):
        json_to_python = json.loads(payload)

        for key, value in json_to_python.items():
            print("Key: {0}\nValue: {1}\n".format(key, value))

    # GET
    def do_GET(self):
        print(self.headers)

        # Send response status code
        # self.send_response(200)
        self._set_response()


        # Send headers
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        print("Payload: ")
        # print(post_data)

        self._set_response()
        self._process_payload(post_data)

        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))



def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, WebHookListener)
    print('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("\nShutting Down Server")

run()