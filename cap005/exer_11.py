deposito = float(input("Deposito inicial: ").strip())
juros = float(input("Juros a.m.: ").strip())

mes_ini = 0
mes_fim = 24

dep = deposito

while mes_ini < mes_fim:
    mes_ini = mes_ini + 1
    dep = dep + (deposito * (juros/100))
    print(f"Mes {mes_ini:02} - Valor: R$ {dep:.2f}")
print(f"O ganho obtido com os juros foi de R$ {dep - deposito:.2f}")
