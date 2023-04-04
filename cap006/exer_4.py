ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'fila atual: {fila}')
    print('digite F para adicionar um cliente ao fim da fila, ')
    print('ou A para realizar o atendimento. S para sair. ')
    operacao = ' '
    while operacao not in 'FfAaSs':
        operacao = str(input('operacao (F, A ou S): ').strip().lower())
        print('operaaco invalida. digite apenas F, A ou S')
        if operacao == 'a':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'cliente {atendido} atendido')
            else:
                print('fila vazia!')
        elif operacao == 'f':
            ultimo += 1
            fila.append(ultimo)
    if operacao == 's':
        break


# Se não verificarmos que a lista está vazia antes de charmos pop(),
# o programa pára com uma mensagem de erro, informando que tentamos
# retirar um elemento de uma lista vazia.
# A verificação é necessária para controlar este erro e assegurar
# o bom funcionamento do programa.
