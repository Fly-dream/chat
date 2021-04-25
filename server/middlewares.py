import zlib
from functools import wraps

def compressioning_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        bytes_request = zlib.decompress(request)
        bytes_responce = func(bytes_request, *args, **kwargs)
        return zlib.compress(bytes_responce)
    return wrapper



def encryption_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        #decrypt request
        bytes_responce = func(request, *args, **kwargs)
        # encrypt responce
        return bytes_responce
    return wrapper