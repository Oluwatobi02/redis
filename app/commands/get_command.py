def make_get():
    def get(key, store):
        value = store.get(key)
        return f"+{value}\r\n".encode("utf-8")
    return get