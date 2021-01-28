def main():
    num = 0
    n = 10

    for i in range(n):
        qn = int(input("Introdueix codi:"))
        num += qn

    print(num / n)


if __name__ == "__main__":
    main()
