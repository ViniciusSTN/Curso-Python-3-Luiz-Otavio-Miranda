# strip -> tira espaços
# lstrip -> tira espaços da esquerda
# rstrip -> tira espaços da direita

# split -> divide uma string e retora lista
# join -> une uma string

frase = '    Olha só que,    coisa interesante     '
lista_palavras = frase.split() # por padrão separa nos espaços
print(lista_palavras)

lista_frases = frase.split(',') # por padrão separa nos espaços
print(lista_frases)


lista_frases2 = []
for i, frase in enumerate(lista_frases):
  lista_frases2.append(lista_frases[i].strip())

print(lista_frases2)

sla = '-'.join('abc')
print(sla)

frases_unidas = ', '.join(lista_frases2)
print(frases_unidas)
