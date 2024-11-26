
def make_echo():
    def echo(message="PONG"):
        return f"+{message}\r\n".encode("utf-8")
    return echo
