salario = float(input("Digite seu salario: "))
aumento10 = (salario * (10/100))
aumento15 = (salario * (15/100))

if salario <= 1250:
    print(f"Seu aumento será de: R${aumento15:.2f}")
else:
    print(f"Seu aumento será de: R$ {aumento10:.2f}")
