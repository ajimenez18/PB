def main():
    num1 =int(input("Introdueix un numero: "))
    num2 =int(input("Introdueix un numero: "))

    if num1 > num2:
        a = num1
        b = num2
    else:
        b = num1
        a = num2

    while b:
        mcd = b
        b = a % b
        a = mcd

    print("El màxim comú divisor de {0} y {1} es {2}".format(num1, num2, mcd))

if __name__ == "__main__":
    main()
