def show_multiplication_table(numbero):
    print(f"Tabla de multiplicar del {numbero}:")

    for i in range(1, 11):
        print(f"{numbero} x {i} = {numbero * i}")

def main():
    numbero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    show_multiplication_table(numbero)

if __name__ == "__main__":
    main()