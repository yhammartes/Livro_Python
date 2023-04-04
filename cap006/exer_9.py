lista = [15, 7, 27, 39]
valor1 = int(input())
valor2 = int(input())
x = 0
achou1 = False
achou2 = False

while x < len(lista):
    if lista[x] == valor1:
        achou1 = True
        break
    if lista[x] == valor2:
        achou2 = True
    x += 1

if achou1:
    print(f'{valor1} encontrado na posicao {lista.index(valor1)}')
elif achou2:
    print(f'{valor2} encontrado na posicao {lista.index(valor2)}')
else:
    print(f'{valor1} e {valor2} nao foram encontrados')
