valor = str(input())
cont = 0
lista = []

while cont < len(valor):
    if valor[cont] == '(':
        lista.append('(')
    if valor[cont] == ')':
        if len(lista) > 0:
            topo = lista.pop(-1)
        else:
            lista.append(')')
            break
    cont += 1


if len(lista) == 0:
    print('OK')
else:
    print('Erro')
