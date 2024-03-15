import random

def generar_numero_aleatorio():
    """Genera un número aleatorio entre 1 y 10."""
    return random.randint(1, 10)

def main():
    continuar = True

    while continuar:
        numero = generar_numero_aleatorio()
        print("Número aleatorio generado:", numero)

        

    print("Fin del programa.")

if __name__ == "__main__":
    main()