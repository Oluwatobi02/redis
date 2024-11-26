import socket  # noqa: F401
import threading

def handle_connection(connection, address):
    while connection.recv(8000):
        connection.send(b"+PONG\r\n")
        print("PONG")
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        connection, address = server_socket.accept()
        thread = threading.Thread(target=handle_connection, args=(connection, address))
        thread.start()

if __name__ == "__main__":
    main()