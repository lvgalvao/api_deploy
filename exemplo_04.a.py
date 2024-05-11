from fastapi import FastAPI
import random
import time
from fastapi.responses import JSONResponse

servidor = FastAPI()

@servidor.get('/recurso')
def numero_aleatorio() -> int:
    num = random.randint(1,60)
    print(num)
    return num

@servidor.get('/recursos')
def numero_aleatorio() -> JSONResponse:
    num = random.randint(1,60)
    print(num)
    return {"data": num}

@servidor.get('/recursos/{numero}')
def numero_que_eu_quero(numero: int) -> JSONResponse:
    return {"data": f"{numero}"}