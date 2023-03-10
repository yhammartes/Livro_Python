n = float(input())
b = 2

# abs = ABSOLUTO - abs(1) retorna 1, abs(-1) retorna 1

while abs(n - (b * b)) > 0.0001:
    p = (b + (n / b)) / 2
    b = p
print(f'A raiz quadrada de {n} é aproximadamente {p:.4f}')
