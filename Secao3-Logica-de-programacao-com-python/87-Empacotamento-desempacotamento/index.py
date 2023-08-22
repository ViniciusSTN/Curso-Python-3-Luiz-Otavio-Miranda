# nome1, nome2, *resto = ['Maria', 'Helena', 'Luiz', 'João']

# por convenção é usado o _ para casos em que não for usado o resto ou a variavel
# nome1, nome2, *_ = ['Maria', 'Helena', 'Luiz', 'João']

_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz', 'João']

# é possivel que o resto seja vazio quando não há mais nada para pegar

print(nome3)
# print(resto)
