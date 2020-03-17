import random
import time

def getId():
    return time.time() * 100 + random.randint(0,9999)