from app.commands import Command
def make_get_handler():
    def handle_get(*args, store):
        return Command.get(*args, store=store)
    return handle_get