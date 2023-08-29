a, b = 1, 2
a, b = b, a

pessoa = {
  'nome': 'Aline',
  'sobrenome': 'Souza'
}

a, b = pessoa.values()
print(a, b, '\n')

a, b = pessoa.items()
print(a, b, '\n')

(a, b), (c, d) = pessoa.items()
print(a, b, c, d, '\n')

for chave, valor in pessoa.items():
  print(chave, valor,)


# ---------------------------------
print('\n')

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

# --------------------------------------------------

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)

#                            args  |       kwargs
mostro_argumentos_nomeados(1, 2, 3, nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
