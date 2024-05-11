import random
import time

def numero_aleatorio() -> int:
    return random.randint(1,60)

def dobra_um_numero(x: int) -> int:
    return x*2

def main():
    num = numero_aleatorio()
    return dobra_um_numero(num)

if __name__ == "__main__":
    while True:
        num_dobrado = main()
        print(num_dobrado)
        time.sleep(1)