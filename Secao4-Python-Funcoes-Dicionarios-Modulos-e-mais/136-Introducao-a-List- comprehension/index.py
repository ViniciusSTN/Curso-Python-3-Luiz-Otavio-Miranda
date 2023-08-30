# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.


print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)


lista2 = [1 for numero in range(10)]
print(lista2)


lista3 = [numero for numero in range(10)]
print(lista3)


lista4 = [
    numero * 2
    for numero in range(10)
]
print(lista4)
