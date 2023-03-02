velocidade = int(input("Qual a velocidade: "))

if velocidade > 80:
    multa = ((velocidade - 80) * 5)
    print(f"Voce levou uma multa de R$ {multa:.2f}")
else:
    print("Dentro do limite")
