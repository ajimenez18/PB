def main():
    num = int(input("Introdueix un nombre entre el 1 i el 10: "))  # Introduce valor de la opción por teclado

    while num > 10:
        print("Nombre incorrecte!")
        num = int(input("Introdueix un nombre entre el 1 i el 10: "))

    print("El numero introduit es", num)


if __name__ == "__main__":
    main()
