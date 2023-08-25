def criar_multiplicador(mult):
  def multiplicar(numero):
    return numero * mult
  return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
