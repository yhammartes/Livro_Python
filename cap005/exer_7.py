n = int(input("Tabuada: "))
inicio = int(input("De: "))
fim = int(input("Até: "))
x = inicio


while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
