import socket
import threading
from app.validation import parsedata as parse
from app.store.key_value_store import key_value_store
from app.handlers import handle
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
            handler, handler_type = handle(command)
            if not handler or handler_type == 'NONE':
                break
            if handler_type == "STORE COMMANDS":
                response = handler(*parts[1:],store= kvs)
                print(response)
            elif handler_type == "PRINT COMMANDS":
                response = handler(*parts[1:])
            
            connection.sendall(response)

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