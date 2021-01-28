def main():
    num1 = int(input("Introdueix el primer numero: "))
    num2 = int(input("Introdueix el numero limit: "))
    i = 0
    j = 0
    x = 0

    for i in range(num1, num2 + 1):
        prime = True
        for j in range(2, 11):
            if i == j:
                break
            elif i % j == 0:
                prime = False
        if prime == True:
            print(' ', i, end='')
            x += 1


if __name__ == "__main__":
    main()
