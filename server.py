import socket

HOST = "0.0.0.0"
PORT = 5000

# Data store
store = {}


def handle_command(command):
    parts = command.split("|")

    if not parts:
        return "ERROR|Invalid command"

    operation = parts[0].upper()

    if operation == "INSERT":
        if len(parts) != 3:
            return "ERROR|INSERT requires key and value"

        key = parts[1]
        value = parts[2]

        if key in store:
            return "ERROR|Key already exists"

        store[key] = value
        return "SUCCESS|Record inserted"

    elif operation == "LOOKUP":
        if len(parts) != 2:
            return "ERROR|LOOKUP requires key"

        key = parts[1]

        if key not in store:
            return "ERROR|Key not found"

        return f"SUCCESS|{store[key]}"

    elif operation == "UPDATE":
        if len(parts) != 3:
            return "ERROR|UPDATE requires key and value"

        key = parts[1]
        value = parts[2]

        if key not in store:
            return "ERROR|Key not found"

        store[key] = value
        return "SUCCESS|Record updated"

    elif operation == "DELETE":
        if len(parts) != 2:
            return "ERROR|DELETE requires key"

        key = parts[1]

        if key not in store:
            return "ERROR|Key not found"

        del store[key]
        return "SUCCESS|Record deleted"

    elif operation == "COUNT":
        return f"SUCCESS|{len(store)}"

    elif operation == "LIST":
        keys = ",".join(store.keys())
        return f"SUCCESS|{keys}"

    else:
        return "ERROR|Unknown command"


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"[SERVER] Listening on {HOST}:{PORT}...", flush=True)

        conn, addr = server_socket.accept()

        with conn:
            print(
                f"[SERVER] Connection established from {addr}",
                flush=True
            )

            while True:
                data = conn.recv(1024)

                if not data:
                    break

                request = data.decode("utf-8").strip()

                print(
                    f"[SERVER] Received request: {request!r}",
                    flush=True
                )

                response = handle_command(request)

                conn.sendall(response.encode("utf-8"))

                print(
                    f"[SERVER] Sent response: {response!r}",
                    flush=True
                )

    print("[SERVER] Connection closed. Shutting down.", flush=True)


if __name__ == "__main__":
    main()