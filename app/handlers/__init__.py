from app.handlers.handle_echo import make_echo_handler
from app.handlers.handle_get import make_get_handler
from app.handlers.handle_ping import make_ping_handler
from app.handlers.handle_set import make_set_handler

handle_echo = make_echo_handler()
handle_ping = make_ping_handler()
handle_set = make_set_handler()
handle_get = make_get_handler()



command_handlers: dict[dict] = {
    "PRINT COMMANDS": {
    "PING": handle_ping,
    "ECHO": handle_echo,
    },
    'STORE COMMANDS': {
        "SET": handle_set,
        "GET": handle_get,
    }
}

def handle(command: str):
    if command in command_handlers['STORE COMMANDS']:
        return command_handlers["STORE COMMANDS"][command], 'STORE COMMANDS'
    elif command in command_handlers['PRINT COMMANDS']:
        return command_handlers["PRINT COMMANDS"][command], 'PRINT COMMANDS'
    return None, 'NONE'
    