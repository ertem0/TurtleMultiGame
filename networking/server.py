import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER_IP, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONECT"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} has connected.")
    
    connected = True
    while connected:
        data = conn.recv(1240).decode(FORMAT)
        print(f"[{addr}]{data}")
        if data == DISCONNECT_MSG:
            connected = False

    conn.close()

def start_server(_server):
    print("[STARTING] Server is starting...")
    _server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = _server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

start_server(server)



print("done!")