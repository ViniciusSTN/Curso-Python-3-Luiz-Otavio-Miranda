# tipo list - mutável (pode alterar os indices)
# list == array (JS)

# Métodos úteis: append, insert, pop, del, clear, extend, +

lista = []
print(lista, type(lista))

print(bool(lista)) # falsy

# ---------------------------------------------------
lista2 = [123, True, 'Olá', []]

# mover muitos itens de listas podem usar muito processamento
del lista2[2] # deleta o indice 2

lista2.append(50) # adiciona ao final da lista

# pode receber parâmetro indicando o indice para remover
valor = lista2.pop(0) # remove o indice 0
ultimo = lista2.pop() # remove o ultimo; OBS: retorna ou não o ultimo valor
print(valor, ultimo)

print(lista2)
