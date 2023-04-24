lista1 = set(map(int, input().split()))
lista2 = set(map(int, input().split()))

print(f"Antes: {lista1}")
print(f"Depois: {lista2}")
print(f"Elementos que não mudaram: {lista1 & lista2}")
print(f"Elementos novos: {lista2 - lista1}")
print(f"Elementos que foram removidos: {lista1 - lista2}")
