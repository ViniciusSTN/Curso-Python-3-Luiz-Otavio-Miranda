# Dictionary Comprehension e Set Comprehension

# Obs: não usar Comprehension com tupla pois gera generator

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

dc2 = {
    chave: valor
    for chave, valor in lista
}

# Set Comprehension
s1 = {2 ** i for i in range(10)}
print(s1)
