import socket
import threading

class Server:
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    PORT = 12345
    ADDR = (SERVER_IP, PORT)
    FORMAT = "utf-8"
    DISCONNECT_MSG = "!DISCONNECT"
    is_online = False

    current_connections = []

    def __init__(self, max_players=4):
        self.max_players = max_players
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} has connected.")
        self.current_connections.append(conn)
        print(self.current_connections)

        connected = True
        while connected:
            try:
                data = conn.recv(1240).decode(self.FORMAT)
            except ConnectionResetError:
                connected = False
                break
                
            print(f"[{addr}] {data}")
            if data == self.DISCONNECT_MSG:
                conn.send(self.DISCONNECT_MSG.encode(self.FORMAT))
                connected = False
                break
            
            self.send_all_conn(data, conn)

        self.current_connections.remove(conn)
        conn.close()
        print(f"[CONNECTION] {addr} Connection closed.")

    def start_server(self):
        print("[STARTING] Server is starting...")
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER_IP}.")
        self.is_online = True

        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr,))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {len(current_connections)}")

    def send_all_conn(self, data, sender):
        print(self.current_connections)
        for conn in self.current_connections:
            if conn != sender:
                conn.send(data.encode(self.FORMAT))


#server = Server()