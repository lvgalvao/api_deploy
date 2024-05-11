import time

def dobra_um_numero(x: int) -> int:
    return x*2

def ler_ultimo_numero() -> int:
    with open('recursos/numeros.txt', 'r') as file:
        numeros = file.readlines()
        return int(numeros[-1])
    

def main():
    num = ler_ultimo_numero()
    return dobra_um_numero(num)

if __name__ == "__main__":
    while True:
        num_dobrado = main()
        print(num_dobrado)
        time.sleep(1)