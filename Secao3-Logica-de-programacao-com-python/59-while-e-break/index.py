condicao = True

while condicao:
  nome = input('Qual seu nome? ')
  print(f'Seu nome é {nome}')

  if nome == 'sair':
    break

print('Acabou')

# ----------------------------------

contador = 0

while contador < 10:
  print(contador)
  contador += 1

print('Acabou')
