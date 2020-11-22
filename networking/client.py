import socket
import threading

class Client:
    SERVER_IP = "192.168.1.91"
    PORT = 12345
    ADDR = (SERVER_IP, PORT)
    FORMAT = "utf-8"
    DISCONNECT_MSG = "!DISCONNECT"
    
    connected = False
    raw_data = b""

    def __init__(self, player=None):
        self.player = player

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.getter_thread = threading.Thread(target=self.get_server_data)
        self.sender_thread = threading.Thread(target=self.send_server_data)


    def connect(self, addr=ADDR):
        print(f"[CONNECTING] client is connecting to {self.SERVER_IP}.")
        try:
            self.client.connect(addr)
        except ConnectionRefusedError:
            print("[CONNECTION] Can't connect to the server.")
            return
        self.connected = True
        self.getter_thread.start()
        self.sender_thread.start()

    def get_server_data(self):
        print("[GETTING DATA]")
        while self.connected:
            data = self.client.recv(2048).decode(self.FORMAT)
            if data == self.DISCONNECT_MSG:
                self.connected = False

            print(f"[DATA] {data}")

        self.client.close()
        

    def send_server_data(self):
        print("[SENDING DATA]")
        while self.connected:
            data = input().encode(self.FORMAT)
            if self.connected:
                self.client.send(data)


#client = Client()
