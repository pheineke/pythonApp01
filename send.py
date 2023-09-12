import socket

# Setze die IP-Adresse und den Port, auf dem du broadcasten möchtest
IP = 'localhost'
PORT = 65000

# Erstelle einen Socket und setze ihn auf Broadcast-Modus
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Frage den Benutzer nach der Eingabe und sende sie als Broadcast
message = input('Gib eine Nachricht ein: ')
sock.sendto(message.encode(), (IP, PORT))

# Schließe den Socket
sock.close()
