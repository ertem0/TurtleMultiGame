import socket
import time

server_ip = "127.0.0.1" #socket.gethostname()
port = 12345

with socket.socket(socket.AF_INET) as s:
    s.bind((server_ip, port))
    s.listen(4)
    print("listening for connections")
    conn, adrr = s.accept()
    with conn:
        print("got a connection from", adrr)
        conn.sendall(b"thank you for connecting")
        conn.close()

print("done!")
        