# nao é usado

string = 'Valor qualquer'

i = 0
while i < len(string):
  letra = string[i]

  # if letra == ' ':
  #   break

  print(letra)
  i += 1
else:
  print('Caiu no else') # sempre cai no else, a não ser que encontre um break no meio do código

print('Fora do laço')
