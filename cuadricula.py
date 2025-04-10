import os

def contador():
    contador1 = "Contador Izq: "
    contador2 = "Contador Der: "
    print(contador1 + contador2.rjust(88))


def cuadricula():
    columns, lines = os.get_terminal_size()
    margen = 3

    print("╔" + "═" * (columns - margen) + "╗")

    for i in range(lines - 8):
        print("║" + "*" * (columns - margen)+"║")

    print("╚" + "═" * (columns - margen) + "╝")


def registros():
    print("Registro 1:")
    print("Registro 2:")
    print("Registro 3:")


def main():
    contador()
    cuadricula()
    registros()


if __name__ == "__main__":
    main()