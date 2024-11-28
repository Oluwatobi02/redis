from app.commands import Command
def make_ping_handler():
    def handle_ping(*args):
        if not args:
            return Command.ping(None)
        return Command.ping(args[0])
    return handle_ping