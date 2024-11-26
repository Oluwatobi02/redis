from app.commands import Command
def make_get_handler():
    def handle_get(*args):
        return Command.get(*args)
    return handle_get