L = [3, 3, 1, 5, 4]
lista = []
fim = len(L)
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    lista.append(e)

print(lista)

# O PROGRAMA FUNCIONARÁ DO MESMO JEITO, DEIXANDO OS
# NUMERO EM ORDEM MESMO REPETIDO
