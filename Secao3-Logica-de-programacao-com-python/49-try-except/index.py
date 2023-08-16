
# try:
#   ...
# except:
#   ...

numero_str = input('Informe um numero: ')
is_digit = numero_str.isdigit() # testa se é um digito retorna True ou False

try:
  numero_float = float(numero_str)
  print('FLOAT: ', numero_float)
  print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except:
  print('Isso não é um número')
  
