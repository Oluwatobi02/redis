def make_get():
    def get(key, store):
        value_object = store.get(key)
        is_object_valid = process_get(value_object)
        if is_object_valid:
            return f"+{value_object['value']}\r\n".encode("utf-8")
        return f"+None\r\n".encode("utf-8")
    return get

import time



def process_get(val_object):
    valids = []
    if 'px' in val_object:
        valids.append(not has_key_expired(val_object['px']))
    return all(valids)
        

def has_key_expired(time_stamp):
    is_expired = time_stamp < time.time()
    return is_expired