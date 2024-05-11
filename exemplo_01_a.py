import random
import time

def numero_aleatorio() -> int:
    return random.randint(1,60)

if __name__ == "__main__":
    while True:
        num = numero_aleatorio()
        print(num)
        time.sleep(1)