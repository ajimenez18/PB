def main():
    n = 5
    llista = []

    for i in range(n):
        num = int(input("Introdueix un numero: "))
        llista.append(num)

    print(llista)
    print("SUMA DE LA LLISTA")
    print(sum(llista))

if __name__ == "__main__":
    main()