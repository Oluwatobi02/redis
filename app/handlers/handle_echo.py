from app.commands import Command
def make_echo_handler():
    def handle_echo(*args):
        return Command.echo(args[0])
    return handle_echo