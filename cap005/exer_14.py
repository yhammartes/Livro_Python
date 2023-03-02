s = 0
qtd = 0

while True:
    v = int(input())
    if v == 0:
        break
    s += v
    qtd += 1
print(s)
print(qtd)
print(f"{s / qtd}")
