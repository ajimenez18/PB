def main():
    num = 1
    valor = 1

    for num in range(11):
        print('\n')
        print("Taula de multiplicar del ", num)
        for valor in range(1, 11):
            print(num, " x ", valor, "=", num * valor)


if __name__ == "__main__":
    main()
