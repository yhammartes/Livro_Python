qtd_kWh = float(input("Quantidade de kWh: "))
tipo_inst = str(input("Tipo de instalacao (R, C, I): ").upper())


if tipo_inst == "R" and qtd_kWh <= 500:
    valor = qtd_kWh * 0.40

elif tipo_inst == "R" and qtd_kWh > 500:
    valor = qtd_kWh * 0.65

if tipo_inst == "C" and qtd_kWh <= 1000:
    valor = qtd_kWh * 0.55

elif tipo_inst == "C" and qtd_kWh > 1000:
    valor = qtd_kWh * 0.60

if tipo_inst == "I" and qtd_kWh <= 5000:
    valor = qtd_kWh * 0.55

elif tipo_inst == "I" and qtd_kWh > 5000:
    valor = qtd_kWh * 0.60

print(f"Valor a pagar: R$ {valor:.2f}")


# RESPOSTA DO LIVRO

consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")
if tipo == "R":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "I":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "C":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preço
print(f"Valor a pagar: R$ {custo:7.2f}")
