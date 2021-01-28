def main():
    seg = int(input("Introdueix els segons: "))

    d = seg // (24 * 60 * 60)
    seg = seg % (24 * 60 * 60)
    h = seg // (60 * 60)
    seg = seg % (60 * 60)
    min = seg // 60
    seg = seg % 60

    print("Dies: {}   Hores: {}   Minuts: {}  Segons: {}".format(d, h, min, seg))


if __name__ == "__main__":
    main()
