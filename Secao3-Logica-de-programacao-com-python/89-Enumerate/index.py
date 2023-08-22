lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# enumera
lista_enumerada = enumerate(lista)
# lista_enumerada = enumerate(lista, start=10) # começa no 10

for item in lista_enumerada:
  print(item) # (0, 'Maria')...

# só funciona uma vez a inumeração
for item in lista_enumerada:
  print(item) # não retorna nada

# para contornar isso basta colocar o enumerate direto no for in
for indice, nome in enumerate(lista):
  print(indice, nome) # 0 Maria

# cria uma lista de tuples
lista_enumerada = list(enumerate(lista)) 
print(lista_enumerada) # [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]