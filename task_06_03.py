from collections import namedtuple


def return_namedtuple(*names):
    def decorator(func):
        def wrapper(*args,**kwargs):
            first_tuple = func(*args,**kwargs)
            if isinstance(first_tuple, tuple):
                s = [*names]
                if len(s) != len(first_tuple):
                    raise ValueError('Invalid names')
                new_tuple = namedtuple('new_tuple',[*names])
                p = new_tuple(*first_tuple)
                #print(p.two)
                return p

            return first_tuple
        return wrapper
    return decorator