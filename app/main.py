import socket  # noqa: F401
import threading

def handle_connection(connection: socket.socket, address):
    while connection:
        data = connection.recv(8000)
        if not data:
            break
        try:
            message = data.decode("utf-8")
            connection.sendall(b"+PONG\r\n")
            print(f"Received: {message}")
        except UnicodeDecodeError:
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