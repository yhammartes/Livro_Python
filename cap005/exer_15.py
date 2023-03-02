result = 0

lista = {1: 0.50, 2: 1, 3: 4, 5: 7, 9: 8}

while True:
    cod = int(input("Codigo do produto: "))
    if cod == 0:
        break
    if cod in lista:
        qtd = int(input("Quantidade: "))
        result = (lista[cod] * qtd) + result
    else:
        print("Codigo invalido")

print(f"Total: R$ {result:.2f}")
