import socket
import threading

SERVER_IP = "192.168.1.91"
PORT = 12345
ADDR = (SERVER_IP, PORT)
FORMAT = "utf-8"

raw_data = b""

def get_server_data(_client):
    print("yo")
    connected = True
    while connected:
        #raw_data = client.recv(2048).decode(FORMAT)
        _client.send(input().encode(FORMAT))
        print(raw_data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTING] client is connecting to {SERVER_IP}.")

thread = threading.Thread(target=get_server_data, args=(client,))
thread.start()

