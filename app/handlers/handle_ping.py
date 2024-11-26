from app.commands import Command
def make_ping_handler():
    def handle_ping(*args):
        return Command.ping(args[0])
    return handle_ping