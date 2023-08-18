frase = 'O Python é uma linguagem de programação ' \
  'multiparadigma. ' \
  'Python foi criado por Guido van Rossum.'

print(frase.count('Phyton')) # count conta quantas ocorrências tem na string

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''
while i < len(frase):
  letra_atual = frase[i]

  if (letra_atual == ' '):
    i += 1
    continue
  
  qtd_vezes_apareceu_atual = frase.count(letra_atual)

  if qtd_apareceu_mais < qtd_vezes_apareceu_atual:
    qtd_apareceu_mais = qtd_vezes_apareceu_atual
    letra_apareceu_mais = letra_atual

  print(letra_atual, qtd_vezes_apareceu_atual)

  i += 1

print(f'A letra que aparceu mais vezes foi {letra_apareceu_mais} = {qtd_apareceu_mais}x')