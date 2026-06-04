from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

current_active_tier = "TIER_0"

class SafetyGatewayServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global current_active_tier
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(current_active_tier.encode())

    def log_message(self, format, *args):
        return

def start_server():
    server = HTTPServer(('0.0.0.0', 8000), SafetyGatewayServer)
    web_thread = threading.Thread(target=server.serve_forever, daemon=True)
    web_thread.start()
    print("🚀 HTTP Telemetry Gateway online on Port 8000...")