# strings são iteráveis

# nome = 'Vinicius'
# print(nome[2])
# print(nome[-6])

# print('a' in nome)
# print('Vin' in nome)

# print('ciu' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} está em {nome}')
else: 
  print(f'{encontrar} não está em {nome}')
