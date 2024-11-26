
def make_ping():
    def ping(message="PONG"):
        return f"+{message}\r\n".encode("utf-8")
    return ping
