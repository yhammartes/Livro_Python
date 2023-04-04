ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'fila atual: {fila}')
    print('digite F para adicionar um cliente ao fim da fila, ')
    print('ou A para realizar o atendimento. S para sair.  ')
    operacao = str(input('operacao (F, A ou S): ').strip().lower())
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x] == 'a':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'cliente {atendido} atendido')
            else:
                print('fila vazia!')
        elif operacao[x] == 'f':
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == 's':
            sair = True
            break
        else:
            print('operaaco invalida. digite apenas F, A ou S')
        x += 1
    if sair:
        print(f'fila atual: {fila}')
        break
