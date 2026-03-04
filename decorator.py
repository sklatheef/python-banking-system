import time

def outer_fuc(func):
    def wrapper(*args,**kwrgs):
        time.sleep(5)
        func(*args,**kwrgs)
    return wrapper