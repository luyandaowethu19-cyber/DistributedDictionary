"""
Lab 1: Introduction to Docker containers and Docker Compose
Simple TCP server.

So this server listens on a TCP port, accepts a single client connection,
receives one request message, and sends back one response/acknowledgment
message. 

So this will demonstrate the basic building block of all
distributed systems communication: a TCP socket exchange
between two independent processes (here, two containers).


The line by line comments will also be provided in a separate document.
"""

import socket

HOST = "0.0.0.0"   # listen on all interfaces inside the container
PORT = 5000         # must match the port exposed in docker-compose.yml


def main():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Allow the socket to be reused immediately after the container restarts
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((HOST, PORT))
        server_socket.listen(1)  # queue length of 1: we only expect one client for this lab

        print(f"[SERVER] Listening on {HOST}:{PORT}...", flush=True)

        # Block until a client connects
        conn, addr = server_socket.accept()
        with conn:
            print(f"[SERVER] Connection established from {addr}", flush=True)

            # Receive the request message (up to 1024 bytes is plenty for this lab)
            data = conn.recv(1024)
            request = data.decode("utf-8")
            print(f"[SERVER] Received request: {request!r}", flush=True)

            # Build and send the response message
            response = f"Hello client : '{request}'"
            conn.sendall(response.encode("utf-8"))
            print(f"[SERVER] Sent response: {response!r}", flush=True)

    print("[SERVER] Connection closed. Shutting down.", flush=True)


if __name__ == "__main__":
    main()
