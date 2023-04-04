# frase = input("Digite uma frase para contar as letras:")
# d = {}
# for letra in frase:
#     if letra in d:
#         d[letra] = d[letra] + 1
#     else:
#         d[letra] = 1
# print(d)


frase = input("Digite uma frase para contar as letras:")
d = {}
for letra in frase:
    # Se letra não existir no dicionário, retorna 0
    # se existir, retorna o valor anterior
    d[letra] = d.get(letra, 0) + 1

del d[' ']
print(d)
