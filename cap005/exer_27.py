n = str(input().lower())
n = n.replace(" ", "")
n1 = n[0::]
n2 = n1[::-1]

if n1 == n2:
    print('É um palindromo')

else:
    print('Não é um palindromo')
