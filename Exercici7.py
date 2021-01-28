def main():
    num1 = int(input("Introdueix un nombre enter: "))
    num2 = int(input("Introdueix un nombre enter: "))
    num3 = int(input("Introdueix un nombre enter: "))

    num = (num1 + num2 + num3)

    if num1 == num2 and num2 == num3:

        mult = (num * 3)
        print(mult)

    else:
        print(num)


if __name__ == "__main__":
    main()
