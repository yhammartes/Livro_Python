divida = float(input("Valor inicial da divida: ").strip())
juros = float(input("Juros a.m.: ").strip())
dep_mensal = float(input("Valor a pagar mensalmente: ").strip())

mes = 1

if (divida * (juros / 100) >= dep_mensal):
    print("Sua divida nao sera paga nunca, pois os juros sao superiores ao \
pagamento mensal")

else:
    saldo = divida
    juros_pago = 0
    while saldo > dep_mensal:
        taxa = saldo * juros / 100
        saldo = saldo + taxa - dep_mensal
        juros_pago = juros_pago + taxa
        print(f"Saldo da divida no mes {mes} e de R$ \
{saldo:.2f}")
        mes = mes + 1
    print(
        f"Para pagar uma dívida de R$ {divida:.2f}, a {juros:.2f}% de juros,")
    print(
        f"você precisará de {mes - 1} meses, pagando um total de R$ \
{juros_pago:.2f} de juros.")
    print(
        f"No último mês, você teria um saldo residual de R$ \
{saldo:.2f} a pagar.")


# dívida = float(input("Dívida: "))
# taxa = float(input("Juros (Ex.: 3 para 3%): "))
# pagamento = float(input("Pagamento mensal:"))
# mês = 1
# if (dívida * (taxa/100) > pagamento):
#     print("Sua dívida não será paga nunca, pois os juros são superiores ao \
# pagamento mensal.")
# else:
#     saldo = dívida
#     juros_pago = 0
#     while saldo > pagamento:
#         juros = saldo * taxa / 100
#         saldo = saldo + juros - pagamento
#         juros_pago = juros_pago + juros
#         print(f"Saldo da dívida no mês {mês} é de R${saldo:6.2f}.")
#         mês = mês + 1
#     print(
#         f"Para pagar uma dívida de R$ \
# {dívida:8.2f}, a {taxa:5.2f} % de juros,")
#     print(
#         f"você precisará de {mês - 1} meses, pagando um total de R$ \
# {juros_pago:8.2f} de juros.")
#     print(
#         f"No último mês, você teria um saldo residual de R${saldo:8.2f} a \
# pagar.")
