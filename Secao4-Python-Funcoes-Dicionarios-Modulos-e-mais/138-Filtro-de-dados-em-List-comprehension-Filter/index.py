# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

# prettier print -> print melhorado
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# lista = [n for n in range(10) if n < 5]
# print(lista)

# filter -> if antes do for
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # mapemanto
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # filtro
]
p(novos_produtos)
