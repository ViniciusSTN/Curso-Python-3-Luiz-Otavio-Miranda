# tipo list - mutável (pode alterar os indices)
# list == array (JS)

# Métodos úteis: append, insert, pop, del, clear, extend, +

lista = [10, 20, 30, 40, 50]

# lista.clear()   # limpa a lista -> []

lista.insert(2, 7) # insere o valor 7 no indice 2

lista.insert(200, 5) # caso o indice não existir na lista, adiciona no final

print(lista)

# -----------------------------------------------

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # faz junção de listas
print(lista_c)

lista_a.extend(lista_b) # [1, 2, 3, 4, 5, 6]

# a diferença de + e extend é que o extend não retorna o valor
