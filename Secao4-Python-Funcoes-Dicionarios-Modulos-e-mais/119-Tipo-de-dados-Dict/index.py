# dict -> dicionários em python
# chave e valor
# chaves podem ser: str, int, float, bool, tuple, etc.
# é um tipo mutável, ou seja, é possível alterar valores de chaves

pessoa = {
  'nome': 'Vinicius',
  'sobrenome': 'Santana',
  'enderecos': [
    {'rua': 'iracy pereira', 'numero': 123},
  ],
  0: 0,
  0.0: 0,
  True: False,
  (1,2,3): 'tupla',
}

pessoa2 = dict(nome='vinicius', sobrenome='Santana')

# é possível iterar sobre as chaves do dict
for chave in pessoa:
  print(chave)

# ----------------------------------------------------------------

# adicionar chave e valor
pessoa['idade'] = 30

chave = 'idade'
print(pessoa[chave]) # 30

# deleta a chave 'idade'
del pessoa[chave]

# print(pessoa)

# testa se existe a chave -> retorna o valor da chave ou None
existe = pessoa.get('chave_qualquer') # por padrão retorna None
# existe = pessoa.get('chave_qualquer', 'Não existe esse trem não') # por padrão retorna None
print(existe)

if existe is None:
  print('Não existe')
else:
  print('Existe')
