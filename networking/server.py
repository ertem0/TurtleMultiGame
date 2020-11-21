import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname()) #socket.gethostname()
PORT = 12345
ADDR = (SERVER_IP, PORT)

def handle_client(conn, addr):
    pass

def start_server(_server):
    _server.listen()
    while True:
        print("[STARTING] server is starting...")
        conn, addr = _server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))

server = socket.socket(socket.AF_INET)
server.bind(ADDR)

startserver(server)



print("done!")