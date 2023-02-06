import base64
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler
import socketserver
import datetime
import json

PORT = 8888
channel_secret = '【CHANEL_SECRET】'

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(501)
        self.end_headers()

    def do_POST(self):
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print()
        print("------------------------------------------------------------")
        print(f"[{now}] Request {self.path} ({self.client_address})")
        print()
        print(self.headers)
        print()

        content_length = int(self.headers['content-length'])
        req_body_bytes = self.rfile.read(content_length)

        # Lineから送られたものかを検証する
        header_signature = self.headers['x-line-signature']
        hash = hmac.new(channel_secret.encode('utf-8'),
            req_body_bytes, hashlib.sha256).digest()
        signature = base64.b64encode(hash)

        if header_signature.encode('utf-8') != signature:
            print("Unable to verify signature")
            print(f"{header_signature=}")
            print(f"{signature=}")
            self.send_response(501)
            self.end_headers()
            return
        
        # JSONをデコードする
        try:
            data = json.loads(req_body_bytes)
        except json.JSONDecodeError:
            print(f"Invalid JSON format: {data}")

        # メッセージイベントを抽出
        events = data['events']
        for event in events:
            if event['type'] == 'message' and event['message']['type'] == 'text':
                message = event['message']['text']
                self.on_receive(message)

        # 正常レスポンス
        self.send_response(200)
        self.end_headers()

    def on_receive(self, message):
        print(f"{message=}")
        # Do something ...


def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
