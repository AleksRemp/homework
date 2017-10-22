import sys


def run_on_linux(func):
    def wrapper(*args,**kwargs):
        if sys.platform == 'linux':
            return func(*args,**kwargs)
        else:
            return None
    return wrapper



def run_on_macos(func):
    def wrapper(*args,**kwargs):
        if sys.platform == "darwin":
            return func(*args, **kwargs)
        else:
            return None
    return wrapper


def run_on_windows(func):
    def wrapper(*args,**kwargs):
        if sys.platform == 'win32':
            return func(*args,**kwargs)
        else:
            return None
    return wrapper