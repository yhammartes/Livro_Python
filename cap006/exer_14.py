# L = [7, 4, 3, 12, 8]
# lista = []
# fim = len(L)
# while fim > 1:
#     trocou = False
#     x = 0
#     while x < (fim - 1):
#         if L[x] > L[x + 1]:
#             trocou = True
#             temp = L[x]
#             L[x] = L[x + 1]
#             L[x + 1] = temp
#         x += 1
#     if not trocou:
#         break
#     fim -= 1
# for e in L:
#     lista.append(e)

# print(lista)

L = [1, 2, 3, 4, 5]
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

# A LISTA SIMPLESMENTE SERA REPETIDA
