import socket  # noqa: F401
import threading
from app.validation import parsedata as parse
from app.commands import Command
from app.store.key_value_store import key_value_store
kvs = key_value_store()

def handle_connection(connection: socket.socket, address):
    while connection:
        data = connection.recv(8000)
        if not data:
            break
        try:
            message = data.decode("utf-8").strip('\r\n')
            parts = parse.parse_resp(message)

            if parts[0] == "PING":

                if len(parts) > 1:
                    connection.sendall(Command.ping(parts[1]))
                else:
                    connection.sendall(Command.ping())
            elif parts[0] == "ECHO":
                if len(parts) > 1:
                    connection.sendall(Command.echo(parts[1]))
                else:
                    connection.sendall(Command.echo())
            elif parts[0] == "SET":
                if len(parts) > 2:
                    connection.sendall(Command.set(parts[1], parts[2], kvs))
            elif parts[0] == "GET":
                if len(parts) > 1:
                    connection.sendall(Command.get(parts[1], kvs))
        except Exception as e:
            print(f"{e}")
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


if __name__ == "__main__":
    main()