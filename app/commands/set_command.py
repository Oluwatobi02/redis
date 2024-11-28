def make_set():
    def set(*args, store):
        args = format_args(args)
        
        store.set(args['key'], args)
        return "+OK\r\n".encode("utf-8")
    return set
import time
def convert_to_unix_timestamp(time_in_ms):
    return time.time() + time_in_ms

def format_args(args: tuple):
    hashmap = {
        'key': args[0],
        'value': args[1]
    }
    if 'px'  in args or 'PX' in args:
        time_to_expire_in_ms = float(args[args.index('px')+1]) / 1000
        hashmap['px'] = convert_to_unix_timestamp(time_to_expire_in_ms)
    return hashmap