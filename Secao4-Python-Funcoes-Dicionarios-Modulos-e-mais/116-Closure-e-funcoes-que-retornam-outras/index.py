def criar_saudacao(saudacao):
  def saudar(nome):
    return f'{saudacao}, {nome}!'
  return saudar

falar_bom_dia = criar_saudacao('Bom dia') 
falar_boa_noite = criar_saudacao('Boa noite')
# salva na memória os argumentos para for usado quando executar a função s1 e s2
# o nome disso é closure
print(falar_bom_dia('Vinicius'))
print(falar_boa_noite('Vinicius'))
