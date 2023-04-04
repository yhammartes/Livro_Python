lista1 = []
lista2 = []

while True:
    valor = int(input('primeira lista: '))
    if valor == 0:
        break
    lista1.append(valor)

while True:
    valor = int(input('Segunda lista: '))
    if valor == 0:
        break
    lista2.append(valor)

lista3 = []
x = 0
segunda = lista1[:]
segunda.extend(lista2)

while len(segunda) > x:
    y = 0
    while y < len(lista3):
        if segunda[x] == lista3[y]:
            break
        y += 1
    if y == len(lista3):
        lista3.append(segunda[x])
    x += 1

x = 0

while x < len(lista3):
    print(f'{x}: {lista3[x]}')
    x += 1
