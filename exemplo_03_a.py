from fastapi import FastAPI
import random
import time

servidor = FastAPI()

@servidor.get('/recursos')
def numero_aleatorio() -> int:
    num = random.randint(1,60)
    print(num)
    return num