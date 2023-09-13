import socket
import threading


HOST = "localhost"
PORT = 5050
ADDR = (HOST, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        message_len = int(conn.recv(HEADER).decode(FORMAT))
        if message_len:
            message = conn.recv(message_len).decode(FORMAT)
            
            if message == "!DISCONNECT":
                connected = False

            print(f"[{addr}] {message}")



def start():
    server.listen()

    print(f"[LISTENING] Server is listening on {HOST}")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] Server is starting...")
start()