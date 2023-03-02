a = int(input())
b = int(input())

if a > b:
    print("O primeiro valor é o maior")
if b > a:
    print("O segundo valor é o maior")

# Ao executar o programa, observamos que retorna
#  o print da primeira logica quando o valor de "a" é maior
#  e retorna o print da segunda logica quando "b" é maior

# Se os valores forem iguais, nada será impresso.
# Isso acontece porque a > b e b > a são falsas quando a = b.
# Assim, nem o print de 2, nem o print de 3 serão executados,
#  logo nada será impresso.
