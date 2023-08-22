string = 'ABCD'

lista = ['Maria', 'Helena', 1, 2, 3, 4, 'Eduarda']

p, s, *_, ap, u = lista
# print(p, s, ap, u)

# print iterando sobre a lista
print(*lista)

# ---------------------------------------------------

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# end='' sep=''
print(*salas, sep='\n') 
