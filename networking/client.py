import socket
import threading

class Client:
    SERVER_IP = "192.168.1.91"
    PORT = 12345
    ADDR = (SERVER_IP, PORT)
    FORMAT = "utf-8"
    raw_data = b""

    def __init__(self, player = None):
        self.player = player

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        print(f"[CONNECTING] client is connecting to {self.SERVER_IP}.")

        thread = threading.Thread(target=self.get_server_data)
        thread.start()

    def get_server_data(self):
        print("yo")
        connected = True
        while connected:
            #raw_data = client.recv(2048).decode(FORMAT)
            self.client.send(input().encode(self.FORMAT))
            print(self.raw_data)


client = Client()
