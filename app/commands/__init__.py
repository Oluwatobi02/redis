from app.commands.ping_command import make_ping
from app.commands.echo_command import make_echo
from app.commands.set_command import make_set
from app.commands.get_command import make_get


ping_command = make_ping()
echo_command = make_echo()
set_command = make_set()
get_command = make_get()


class Command:
    def ping(message=""):
        if message:
            return ping_command(message)
        return ping_command()
    
    def echo(message=""):
        if message:
            return echo_command(message)
        return echo_command()
    def set(key, value, store):
        return set_command(key, value, store)
    
    def get(key, store):
        return get_command(key, store)