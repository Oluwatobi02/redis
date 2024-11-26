def make_set():
    def set(key, value, store):
        store.set(key, value)
        return "+OK\r\n".encode("utf-8")
    return set