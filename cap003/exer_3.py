a = True
b = False
c = True

result = [a and a, b and b, not c, not b,
          not a, a and b, b and c, a or c,
          b or c, c or a, c or b, c or c, b or b]

print(result)
