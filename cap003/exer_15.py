cigarros_dia = int(input("Quantidade de cigarros por dia: "))
anos_fumando = int(input("Quantidade de anos fumando: "))
perda_vida = 10  # min

minutos_fumados = perda_vida * cigarros_dia * (anos_fumando * 365)
perda_vida_dia = round(minutos_fumados / 60 / 24)


print(f"Voce perdeu {perda_vida_dia} dias de vida por fumar.")
