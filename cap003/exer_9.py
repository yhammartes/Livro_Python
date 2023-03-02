tempo = input().split(":")
d, h, m, s = int(tempo[-4]), int(tempo[-3]), int(tempo[-2]), int(tempo[-1])
ds = ((d*24)*60)*60
hs = h*60*60
ms = m*60
total = ds + hs + ms + s
print(total)

# resposta do livro
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_segundos = (dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos)
print(f"Convertido em segundos é igual a {total_segundos} segundos.")
