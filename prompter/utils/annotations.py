import logging

def dev_log(func):
    def wrapper(*args, **kwargs):        
        resp = func(*args, **kwargs)
        logging.info(f"Returns: {resp}")
        return resp
    return wrapper

