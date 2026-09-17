import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5050


def send_to_server(message):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(2)

        client.connect((SERVER_HOST, SERVER_PORT))

        client.sendall(message.encode("utf-8"))

        response = client.recv(4096).decode("utf-8")

        print("CN: Connected successfully!")
        print("CN: Message sent:", message)
        print("CN: Server response:", response)

        client.close()

    except Exception as e:
        print("CN connection error:", e)


# Run this file directly to test the network connection
if __name__ == "__main__":
    print("=== CN CLIENT TEST ===")

    send_to_server(
        "Hello from AI Smart Classroom Assistant"
    )