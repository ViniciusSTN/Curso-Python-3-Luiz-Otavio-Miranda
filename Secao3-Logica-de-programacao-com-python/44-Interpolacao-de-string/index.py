# Interpolação básica
# s - string
# d e i - int
# f - float
# x e X - hexadecimal

nome = 'Luiz'
preco = 1000.92835273

# se tiver só um valor não precisa de parenteses
variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)

# x -> hexadecimal minusculo
# X -> hexadecimal maiusculo
# 04 indica que deverá prencher 4 casas pelo menos, completa com 0
print('O hexadecimal de %d é %04X' % (15, 15))
