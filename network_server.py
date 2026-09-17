import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"Network server listening on port {PORT}...")

while True:
    connection, address = server.accept()

    try:
        data = connection.recv(4096).decode("utf-8")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {address} -> {data}")
        connection.sendall(b"Message received by CN server")
    except Exception as e:
        print("Network error:", e)
    finally:
        connection.close()
