row_and_columns = [
  (x, y)
  if y != 2 else (x, y * 2) # map
  for x in range(1, 4) 
  for y in range(1, 6) # for aninhado
  if x != 2 # filter
]
print(row_and_columns)



numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)



nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)



string = 'Otávio Miranda'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])
print(nova_string)
