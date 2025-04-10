import os
contador1 = "Contador Izq: "
contador2 = "Contador Der: "
print(contador1 + contador2.rjust(78))


def cuadricula():
    columns, lines = os.get_terminal_size()
    margen = 3

    print("╔" + "═" * (columns - margen) + "╗")

    for i in range(lines - 2):
        print("║" + "*" * (columns - margen)+"║")

    print("╚" + "═" * (columns - margen) + "╝")


cuadricula()

print("Registro 1:")
print("Registro 2:")
print("Registro 3:")