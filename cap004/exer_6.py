distancia = float(input("Distancia da viagem: "))

distanc200 = distancia * 0.5
distanclonga = distancia * 0.45

if distancia <= 200:
    print(f"O valor da passagem é: R$ {distanc200:.2f}")
else:
    print(f"O valor da passagem é: R$ {distanclonga:.2f}")
