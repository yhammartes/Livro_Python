ultimo = 0
lista1 = []
lista2 = []

while True:
    # print(f'Fila 1: {lista1}')
    # print(f'Fila 2: {lista2}')
    print('F: adiciona fila 1')
    print('G: adiciona fila 2')
    print('A: atende fila 1')
    print('B: atende fila 1')
    print('S: sair')
    op = str(input('operacao (F, G, A, B ou S): ').strip().lower())
    aux = 0
    sair = False

    while aux < len(op):
        if op[aux] == 'f':
            ultimo += 1
            lista1.append(ultimo)

        if op[aux] == 'g':
            ultimo += 1
            lista2.append(ultimo)
            ultimo += 1

        if op[aux] == 'a':
            if len(lista1) > 0:
                atendido = lista1.pop(0)
                print('atendido lista 1: ', atendido)
            else:
                print('fila 1 vazia')

        if op[aux] == 'b':
            if len(lista2) > 0:
                atendido = lista2.pop(0)
                print('atendido lista 2: ', atendido)
            else:
                print('fila 2 vazia')

        if op[aux] == 's':
            sair = True
            break

        else:
            print('operacao invalida')

        aux += 1

    if sair:
        print('fila atual 1', lista1)
        print('fila atual 2', lista2)
        break
