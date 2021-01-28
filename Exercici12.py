def main():
    n = 10
    i = 0
    pares = []
    impares = []

    for i in range(n):
        num = int(input("Introdueix un numero entre el 0 i el 10:"))
        if num < 11:
            i += 1
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        else:
            num = int(input("Malament! Introdueix un numero entre el 0 i el 10:"))

    print("Nombres parells: ", pares)
    print("Nompres senars: ", impares)

if __name__ == "__main__":
    main()