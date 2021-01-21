# Alex Jiménez Pozo

def main():
    print("Hello world")
    i = 0
    n = 15
    ap = 0  # Persones aprovades
    sp = 0  # Persones suspeses
    xa = 0  # Acumula les notes aprovades
    xs = 0  # Acumula les notes suspeses
    map = 0  # Mitjana de les notes aprovades
    msp = 0  # Mitjana de les notes suspeses

    for i in range(n):
        qn = int(input("Introdueix un numero entre el 0 i el 10:"))
        if qn < 11:
            i += 1
        else:
            qn = int(input("¡Malament! Introdueix un numero entre el 0 i el 10:"))

        if qn > 4:
            ap += 1
            xa += qn

        else:
            sp += 1
            xs += qn

    map = (xa / ap)
    msp = (xs / sp)

    print("Mitjana de notes aprovats: ", map)
    print("Mitjana de notes suspeses: ", msp)
    print("Persones que han aprovat: ", ap)
    print("Persones que han suspes: ", sp)


if __name__ == '__main__':
    main()

