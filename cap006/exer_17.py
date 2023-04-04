# estoque = {"tomate": [1000, 2.3],
#            "alface": [500, 0.45],
#            "batata": [2001, 1.20],
#            "feijao": [100, 1.50]
#            }

# venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
# total = 0
# print("Vendas: \n")

# for operacao in venda:
#     produto, quantidade = operacao
#     preco = estoque[produto][1]
#     custo = preco * quantidade
#     print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
#     estoque[produto][0] -= quantidade
#     total += custo
# print(f'Custo total: R${total:21.2f}\n')

# for chave, dados in estoque.items():
#     print("Descricao: ", chave)
#     print("Quantidade: ", dados[0])
#     print(f'Preco: {dados[1]:6.2f}\n')


estoque = {"tomate": [1000, 2.3],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijao": [100, 1.50]
           }
total = 0
print("Vendas: \n")
while True:
    produto = str(input('Produto: ').capitalize())
    if produto == 'Fim':
        break
    if produto in estoque:
        quantidade = int(input('Quantidade: '))
        if quantidade <= estoque[produto[0]]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(
                f'{produto: 12s}: {quantidade: 3d} x \
                {preco: 6.2f} = {custo: 6.2f}')
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print('Produto nao cadastrado')

print(f'Custo total: R${total:21.2f}\n')
print('Estoque: \n')
for chave, dados in estoque.items():
    print("Descricao: ", chave)
    print("Quantidade: ", dados[0])
    print(f'Preco: {dados[1]:6.2f}\n')
