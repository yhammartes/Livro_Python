lista1 = set(map(int, input().split()))
lista2 = set(map(int, input().split()))

comum = lista1 & lista2
v1l = lista1 - lista2
v2l = lista2 - lista1
nl = lista1 ^ lista2

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Valores em comum: {comum}")
print(f"Valores não repetidos só da primeira lista: {v1l}")
print(f"Valores não repetidos só da segunda lista: {v2l}")
print(f"Valores não repetidos: {nl}")
print(f"Primeira lista sem os valores repetidos da segunda: {v1l}")
