# resumo
# lower() # minúsculo
# startswith('s') # começa com s
# endswith('s') # termina com s

while True:
  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operador = input('Digite o operador (+-/*): ')

  numeros_validos = None
  numero_1_float = 0.0
  numero_2_float = 0.0

  try:
    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)
    numeros_validos = True
  except:
    numeros_validos = None

  if numeros_validos is None:
    print('Um ou ambos números são inválidos')
    continue

  operadores_permitidos = '+-/*'

  if operador not in operadores_permitidos:
    print('Operador inválido')
    continue

  if len(operador) > 1:
    print('Digite apenas um operador')
    continue

  print('Realizando sua conta, confira o resultado abaixo: ')

  if operador == '+':
    print(numero_1_float + numero_2_float)
  if operador == '-':
    print(numero_1_float - numero_2_float)
  if operador == '/':
    print(numero_1_float / numero_2_float)
  if operador == '*':
    print(numero_1_float * numero_2_float)

  sair = input('Quer sair? [s]im: ').lower().startswith('s')

  if sair is True:
    break
