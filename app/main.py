import socket  # noqa: F401
import threading

def parse_resp(data):
    lines = data.split("\r\n")
    result = []
    idx = 0

    while idx < len(lines):
        line = lines[idx]
        if line.startswith("*"):  # Array
            array_length = int(line[1:])
            result = []  # Initialize an array
        elif line.startswith("$"):  # Bulk string
            length = int(line[1:])  # Length of the string
            idx += 1  # Move to the next line (actual string)
            result.append(lines[idx][:length])
        idx += 1

    return result


def handle_connection(connection: socket.socket, address):
    while connection:
        data = connection.recv(8000)
        if not data:
            break
        try:
            message = data.decode("utf-8").strip('\r\n')
            parts = parse_resp(message)
            print(parts)
            if parts[0] == "ECHO" and len(parts) > 1:
                connection.sendall(f"+{parts[1]}\r\n".encode("utf-8"))
            elif parts[0] == "PING" and len(parts) > 1:
                connection.sendall(f"+{parts[1]}\r\n".encode("utf-8"))
            else:
                connection.sendall(b"+PONG\r\n")
        except:
            connection.sendall(b"-ERR invalid encoding\r\n")
            continue
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        connection, address = server_socket.accept()
        thread = threading.Thread(target=handle_connection, args=(connection, address))
        thread.start()
        thread.join()

if __name__ == "__main__":
    main()