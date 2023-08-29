# Função lambda
# sorted -> retorna uma shallow copy ordernada
# sort -> orderna o própria lista

lista = [4, 31, 4, 65, 23, 74, 6, 123, 0]

lista.sort()
# lista.sort(reverse=True)

print(lista)

# ------------------------------------------------------

lista2 = [
  {'nome': 'Luiz', 'sobrenome': 'Zimbabue'},
  {'nome': 'Maria', 'sobrenome': 'Oliveira'},
  {'nome': 'Daniel', 'sobrenome': 'Silva'},
  {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
  {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
  return item['sobrenome']

lista2.sort(key=ordena)
print(lista2)


print('\n\n')
# a mesma coisa de forma simples:
lista2.sort(key=lambda item: item['sobrenome'])
print(lista2)

# ------------------------------------------------------
print('\n\n')

# sorted retorna uma shallow copy ordernada
l1 = sorted(lista2, key=lambda item: item["nome"])
print(l1)
