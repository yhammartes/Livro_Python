lista = [15, 7, 27, 39]
valor = int(input())
x = 0

while x < len(lista):
    if lista[x] == valor:
        break
    x += 1

if x < len(lista):
    print(f'{valor} encontrado na posicao {lista.index(valor)}')
else:
    print(f'{valor} nao encontrado')
