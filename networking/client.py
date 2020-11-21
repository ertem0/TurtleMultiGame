

import socket
import time

server_ip = "127.0.0.1" #socket.gethostname()
port = 12345

with socket.socket(socket.AF_INET) as s:
    s.connect((server_ip, port))
    data = s.recv(1024)

print("[From server]", data)