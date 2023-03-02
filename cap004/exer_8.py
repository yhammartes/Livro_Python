a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
op = input("Operação que deseja fazer (+, -, * ou /): ")


if op == "+":
    result = a + b
    print("Resultado:", result)
elif op == "-":
    result = a - b
    print("Resultado:", result)
elif op == "*":
    result = a * b
    print("Resultado:", result)
elif op == "/":
    result = a / b
    print("Resultado:", result)
else:
    print("Dados invalidos")
    result = 0
