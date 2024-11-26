from app.commands import Command
def make_set_handler():
    def handle_set(*args):
        return Command.set(*args)
    return handle_set