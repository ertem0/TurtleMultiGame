import socket
import threading

SERVER_IP = "192.168.1.91"
PORT = 12345
ADDR = (SERVER_IP, PORT)
FORMAT = "utf-8"

def get_server_data(_client):
    connected = True
    while connected:
        data = _client.recv(2048).decode(FORMAT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

thread = threading.Thread(target=get_server_data, args=client)

