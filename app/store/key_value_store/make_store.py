class KeyValueStore:
    def __init__(self, store: dict = {}):
        self.store = store

    def get(self, key: str) -> str:
        return self.store.get(key)

    def set(self, key: str, value: str) -> None:
        self.store[key] = value
    
def make_key_value_store():
    def key_value_store(store: dict = {}):
        return KeyValueStore(store)
    return key_value_store