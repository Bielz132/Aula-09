# ATIVIDADE 1

# Crie um sistema de banco, com as seguintes operações:

# ** Utilize While ou loop **

# # SISTEMA de Mercado: 

# - Dicionarios 
# - Conteúdo dicionário
# - Fazer compra
# - Verificar e pagar

print('------------Seja bem vindo ao Mercadinho!------------')
lojinha = {
'Biscoito': 7.50,    # = 0
'Salgadinho': 12.00, # = 1 
'Macarrão': 3.50,    # = 2
'Molho': 5.00 }      # = 3

produtos = []
valores = []

for n,x in lojinha.items():
    produtos.append(n)
    valores.append(x)
    print(produtos, valores)

carrinho = []
meus_valores = []

print(f'''Aqui, nossos produtos são esses:
Biscoito = R$ 7.50  (0)
Salgadinho = R$ 12.00  (1)
Macarrão = R$ 3.50  (2)
Molho = R$ 5.00  (3)''')


escolha = int(input('Digite o ID do produto: '))
while escolha == 'Biscoito':
    carrinho.append('Biscoito')
    meus_valores.append(7.50)
    print(carrinho,'R$',meus_valores)

# elif escolha == 'Salgadinho':
#     carrinho.append('Biscoito')
#     meus_valores.append(7.50)
#     print(carrinho,'R$',meus_valores)

# elif escolha == 'Macarrão':
#     carrinho.append('Biscoito')
#     meus_valores.append(7.50)
#     print(carrinho,'R$',meus_valores)

# elif escolha == 'Molho':
#     carrinho.append('Biscoito')
#     meus_valores.append(7.50)
#     print(carrinho,'R$',meus_valores)


        
        
