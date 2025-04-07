def tabla_ascii():
    qty = 6
    for i in range(32, 255):
        print(str(i).ljust(4), ": ", chr(i), end="")
        if not (i % qty):
            print()

tabla_ascii()
