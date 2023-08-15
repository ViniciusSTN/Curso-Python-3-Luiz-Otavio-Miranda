a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f} {}'.format(a, b, c, '1234')
formato2 = 'a={1} b={0} c={1} {nome3}'.format(a, b, nome3=c)
# se nomear um parâmetro, os seguintes também precisam ser

# print(formato)
print(formato2)
