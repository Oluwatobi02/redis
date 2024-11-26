import socket
import threading
from app.validation import parsedata as parse
from app.commands import Command
from app.store.key_value_store import key_value_store
from app.handlers import command_handlers
kvs = key_value_store()

def handle_connection(connection: socket.socket, address):
    while connection:
        data = connection.recv(8000)
        if not data:
            break
        try:
            message = data.decode("utf-8").strip('\r\n')
            parts = parse.parse_resp(message)
            command = parts[0]
            handler = command_handlers[command]
            if not handler:
                break
            connection.sendall(handler(*parts[1:], kvs))
            
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