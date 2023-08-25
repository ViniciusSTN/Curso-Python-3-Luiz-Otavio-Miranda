# lembre-se de empacotamento e desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)



def somar(*args):
  total = 0
  for numero in args:
    total += numero
  return total


soma = somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(soma)

# função nativa do python para somar
soma2 = sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(soma2)
