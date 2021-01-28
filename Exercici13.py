def main():
    num1 = int(input("Introdueix un numero: "))
    num2 = int(input("Introdueix un altre numero: "))

    print("Num1 introduit: ", num1)
    print("Num2 introduit: ", num2)

    print("Intercanvi")
    num1, num2 = num2, num1

    print("Num1 introduit: ", num1)
    print("Num2 introduit: ", num2)

if __name__ == "__main__":
    main()