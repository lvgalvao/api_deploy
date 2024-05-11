import random
import time

def numero_aleatorio() -> int:
    num = random.randint(1,60)
    print(num)
    with open('recursos/numeros.txt', 'a') as file:
        file.write(f"{num}\n")

if __name__ == "__main__":
    while True:
        numero_aleatorio()
        time.sleep(1)