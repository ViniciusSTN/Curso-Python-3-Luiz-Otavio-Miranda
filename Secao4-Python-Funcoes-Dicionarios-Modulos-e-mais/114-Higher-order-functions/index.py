def saudacao(msg):
  return msg

def executa(funcao, msg):
  return funcao(msg)

valor = executa(saudacao, 'bom dia')
print(valor)
