
condicao = True

passou_no_if = None

if condicao:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')

print(passou_no_if is None) # False
print(passou_no_if is not None) # True

if passou_no_if is None:
  print('Não passou')
else:
  print('Passou')
