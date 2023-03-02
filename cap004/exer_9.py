valor_casa = float(input("Valor da casa: "))
salario = float(input("Salario: "))
qtd_anos = int(input("Quantidade de anos a pagar: "))

parcelas = qtd_anos * 12
valor_parcelas = valor_casa / parcelas
valor_salario = salario * (30/100)

if valor_salario < valor_parcelas:
    print("Infelizmente voce nao pode obter o emprestimo")
else:
    print(f"Valor da prestacao: R$ {valor_parcelas:.2f} - Emprestimo OK")
