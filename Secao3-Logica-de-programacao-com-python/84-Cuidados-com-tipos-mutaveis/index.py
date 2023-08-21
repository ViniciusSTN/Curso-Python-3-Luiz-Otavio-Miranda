lista_a = ['Vinicius', 'Santana']

# lista_b = lista_a # aponta para mesmo endereço na memória

lista_b = lista_a.copy() # para não apontar para o mesmo endereço de memória
print(lista_b)