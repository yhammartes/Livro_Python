qtd_km = float(input("KM: "))
dias = float(input("Dias: "))
preco_aluguel = 60
preco_km = 0.15

total = (qtd_km * preco_km) + (dias * preco_aluguel)
print(f"Total a pagar: R$ {total:.2f}")
