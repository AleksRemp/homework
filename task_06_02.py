import time

def pause(sec):
    def decorator(func):
        def wrapper(*args,**kwargs):
            #print('Функция выполняется с задержкой!')
            time.sleep(sec)
            return func(*args,**kwargs)
        return wrapper
    return decorator