# len - quantas chaves tem
# keys - iterável com chaves
# values - iterável de valores
# itens - iterável com chave e valor
# setdefault - adiciona valor default

pessoa = {
  'nome': 'Vinicius',
  'Sobrenome': 'Santana',
}

print(len(pessoa)) # 2
print(pessoa.keys()) # dict_keys(['nome', 'Sobrenome'])
print(list(pessoa.keys())) # ['nome', 'Sobrenome']
print(pessoa.values()) # dict_values(['Vinicius', 'Santana'])
print(list(pessoa.values())) # ['Vinicius', 'Santana']

# for chave, valor in pessoa.items():
#   print(chave, valor)

pessoa.setdefault('nome', 'Josefino') # não vai atribuir, pois nome já tem valor
pessoa.setdefault('idade', 21) # vai atribuir default
print(pessoa['nome'])
print(pessoa['idade']) # 21


