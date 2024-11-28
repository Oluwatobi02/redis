from app.commands import Command
def make_set_handler():
    def handle_set(*args, store):
        return Command.set(*args, store=store)
    return handle_set