lista = [15, 7, 27, 39]
valor1 = int(input())
valor2 = int(input())
x = 0
achou1 = -1
achou2 = -1

while x < len(lista):
    if lista[x] == valor1:
        achou1 = x
    if lista[x] == valor2:
        achou2 = x
    x += 1

if achou1 != -1:
    print(f'{valor1} encontrado na posicao {lista.index(valor1)}')
if achou2 != -1:
    print(f'{valor2} encontrado na posicao {lista.index(valor2)}')
else:
    print(f'{valor1} e {valor2} nao foram encontrados')

if achou1 != -1 and achou2 != -1:
    if achou1 <= achou2:
        print('achou1 foi achado antes de achou2')
    else:
        print('achou2 foi achado antes de achou1')
