import socket

# Setze die IP-Adresse und den Port, auf dem du broadcasten möchtest
IP = '0.0.0.0'
PORT = 65000

# Erstelle einen Socket und binde ihn an die IP-Adresse und den Port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

# Höre auf eingehende Broadcasts
while True:
    data, address = sock.recvfrom(1024)
    print(f"Received message: {data.decode()} from {address}")
