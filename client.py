import socket
import time

SERVER_HOST = "server"
SERVER_PORT = 5000
STARTUP_DELAY_SECONDS = 2


def send_request(client_socket, request):
    print(f"[CLIENT] Sending: {request}", flush=True)
    client_socket.sendall(request.encode("utf-8"))

    data = client_socket.recv(1024)
    response = data.decode("utf-8")

    print(f"[CLIENT] Received: {response}", flush=True)
    return response


def main():
    time.sleep(STARTUP_DELAY_SECONDS)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    with client_socket:
        print(
            f"[CLIENT] Connected to {SERVER_HOST}:{SERVER_PORT}",
            flush=True
        )

        # Insert at least three records.
        send_request(
            client_socket,
            "INSERT|202315370|LUYANDA SHOZI"
        )

        send_request(
            client_socket,
            "INSERT|001|Distributed Systems"
        )

        send_request(
            client_socket,
            "INSERT|002|Computer Science"
        )

        # Test COUNT and LIST after inserting records.
        send_request(client_socket, "COUNT")
        send_request(client_socket, "LIST")

        # Delete one record.
        send_request(client_socket, "DELETE|001")

        # Test COUNT and LIST again after DELETE.
        send_request(client_socket, "COUNT")
        send_request(client_socket, "LIST")

    print("[CLIENT] Connection closed.", flush=True)


if __name__ == "__main__":
    main()