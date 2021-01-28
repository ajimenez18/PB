def main():
    a = [10,20,30,20,10,50,60,40,80,50,40]
    b = []

    print("Llista normal: ", a)

    b = set(a)

    print("Llista sense duplicats: ", b)

if __name__ == "__main__":
    main()