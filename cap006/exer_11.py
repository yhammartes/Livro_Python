# NO PROGRAMA 6.6, NO PRIMEIRO WHILE NAO TEMOS UMA QUANTIDADE DE ELEMENSTOS DEFINIDA,
# LOGO, PRECISAMOS UTILIZAR UM LOOPING INFINITO ATÉ TER UMA QUANTIDADE DE ELEMENTOS.

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
for e in L:
    print(e)
