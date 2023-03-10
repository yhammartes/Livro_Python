# tabuada = 1

# while tabuada <= 10:
#     numero = 1
#     while numero <= 10:
#         print(f'{tabuada} x {numero} = {tabuada * numero}')
#         numero += 1
#     tabuada += 1

while True:
    valor = int(input('Digite o valor a pagar: '))
    if valor == 0:
        break

    cedulas = 0
    atual = 200
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
            valor = valor + valor
        else:
            print(f"{cedulas} cedula(s) de R${atual}")
            if apagar == 0:
                break
            if atual == 200:
                atual = 100
            elif atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0
