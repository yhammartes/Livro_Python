T = [-10, -8, 0, 1, 2, 5, -2, -4]

max = T[0]
min = T[0]
soma = 0

for e in T:
    if e > max:
        max = e
    if e < min:
        min = e
    soma += e
print(f'Temperatura minima: {min} °C')
print(f'Temperatura maxima: {max} °C')
print(f'Temperatura media: {soma / len(T)} °C')
