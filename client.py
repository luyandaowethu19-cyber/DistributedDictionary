"""
Lab 1: Introduction to Docker containers and Docker Compose
Simple TCP client.

Connects to the server container over TCP, sends a single
request message, waits for the response, prints it, then
closes the connection.
"""

import socket
import time

# "server" is the service name defined in docker-compose.yml.
# Docker Compose's built-in DNS resolves this name to the server
# container's IP address on the shared network -- this is the
# simplest possible example of a naming service in action.
SERVER_HOST = "server"   
SERVER_PORT = 5000


STARTUP_DELAY_SECONDS = 2


def main():
    time.sleep(STARTUP_DELAY_SECONDS)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    with client_socket:
        print(f"[CLIENT] Connected to {SERVER_HOST}:{SERVER_PORT}", flush=True)

        # Send the request message
        request = "Hello server, this is the client."
        client_socket.sendall(request.encode("utf-8"))
        print(f"[CLIENT] Sent request: {request!r}", flush=True)

        # Wait for the response message
        data = client_socket.recv(1024)
        response = data.decode("utf-8")
        print(f"[CLIENT] Received response: {response!r}", flush=True)

    print("[CLIENT] Connection closed.", flush=True)


if __name__ == "__main__":
    main()