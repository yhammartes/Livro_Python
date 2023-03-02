salario = float(input("Salario: "))
p_aumento = float(input("Porcentagem de aumento: "))

salario_atual = salario + (salario * p_aumento / 100)

print(f"Aumento de: R$ {(salario * p_aumento / 100):.2f}")
print(f"Novo salario: R$ {salario_atual:.2f}")
