# numeros = [0, 0, 0, 0, 0]
# x = 0
# while x < len(numeros):
#     numeros[x] = int(input(f'Numeros {x + 1}: '))
#     x += 1

# while True:
#     escolhido = ' '
#     while escolhido not in '012345':
#         escolhido = str(
#             input('que posicao voce quer imprimir (0 para sair): '))
#     escolhido = int(escolhido)
#     if escolhido == 0:
#         break
#     print(f'{escolhido} = {numeros[escolhido-1]}')


lista1 = []
lista2 = []

while True:
    valor = int(input('Primeira lista: '))
    if valor == 0:
        break
    lista1.append(valor)

while True:
    valor = int(input('Segunda lista: '))
    if valor == 0:
        break
    lista2.append(valor)

lista3 = lista1[:]
lista3.extend(lista2)

x = 0
while len(lista3) > x:
    print(f'{x}: {lista3[x]}')
    x += 1
