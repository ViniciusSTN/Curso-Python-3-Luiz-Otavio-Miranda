# get -> obtém o valor da chave ou none (aula119)

# pop -> a chave e valor da chave informada, também pode retornar o valor da chave removida

# popitem -> remove o ultimo 'indice', retorna tupla de chave e valor removido

# update -> pode atualizar chaves e acrescentar novas (pode ser feito em uma linha ou usando tupla ou lista)


p1 = {
  'nome': 'Vinicius',
  'sobrenome': 'Santana',
}

# chave_removida = p1.pop('nome')
# print(chave_removida)

# ultima_chave = p1.popitem()
# print(ultima_chave)

p1.update({
  'nome': 'Novo nome',
  'idade': 30,
})
# print(p1) # {'nome': 'Novo nome', 'sobrenome': 'Santana', 'idade': 30}

# pode ser feito em uma linha só, mas as chaves precisam ser string
p1.update(nome='Novo nome 2', cor_olhos='preto')
# print(p1) # {'nome': 'Novo nome 2', 'sobrenome': 'Santana', 'idade': 30, 'cor_olhos': 'preto'}

# é possivel alterar usando tupla ou lista
tupla = (('nome', 'Novo nome 3'), ('idade', 40))
tupla2 = [['endereço', 'Iracy Pereira Goulart']]
p1.update(tupla)
p1.update(tupla2)
print(p1) # {'nome': 'Novo nome 3', 'sobrenome': 'Santana', 'idade': 40, 'cor_olhos': 'preto', 'endereço': 'Iracy Pereira Goulart'}
