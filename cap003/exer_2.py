a = 4
b = 10
c = 5.0
d = 1
f = 5

resultado = [a == c, a < b, d > b, c != f,
             a == b, c < d, b > a, c >= f,
             f >= c, c <= c, c <= f]

print(resultado)
