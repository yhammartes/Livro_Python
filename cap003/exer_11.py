preco_prod = float(input("Preço: "))
p_desconto = float(input("Desconto: "))

preco_desc = preco_prod - (preco_prod * p_desconto / 100)

print(f"Desconto: R$ {preco_prod * p_desconto / 100:.2f}")
print(f"Total: R$ {preco_desc:.2f}")
