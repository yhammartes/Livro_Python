# tabuada = 1

# while tabuada <= 10:
#     numero = 1
#     while numero <= 10:
#         print(f'{tabuada} x {numero} = {tabuada * numero}')
#         numero += 1
#     tabuada += 1
# =====================================================================


# numero = 1
# tabuada = 1

# while True:
#     print('''
# Menu
# -----------------
# 1 - Adição
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# 5 - Sair
# -----------------
# ''')
#     op = str(input())
#     if op == '5':
#         break
#     if op == '1':
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f'{tabuada} + {numero} = {tabuada + numero}')
#                 numero += 1
#             tabuada += 1

#     elif op == '2':
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f'{tabuada} - {numero} = {tabuada - numero}')
#                 numero += 1
#             tabuada += 1

#     elif op == '3':
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f'{tabuada} x {numero} = {tabuada * numero}')
#                 numero += 1
#             tabuada += 1

#     elif op == '4':
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f'{tabuada} ÷ {numero} = {tabuada / numero}')
#                 numero += 1
#             tabuada += 1


while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        n = int(input("Tabuada de:"))
        x = 1
        while x <= 10:
            if opção == 1:
                print(f"{n} + {x} = {n + x}")
            elif opção == 2:
                print(f"{n} - {x} = {n - x}")
            elif opção == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif opção == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")
