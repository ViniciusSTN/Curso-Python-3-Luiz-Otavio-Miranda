# iterável -> str, range, etc... -> possuem método (__iter__)
# iterador
# next
# iter

# no ultimo next gera um erro para informar que acabou o número de indices, o erro é tratado e acaba a iteração do for in

iterador = iter('Vinicius') # .__iter__()
print(iterador)

# print(next(iterador)) # .__next__()

while True:
  try:
    print(next(iterador))
  except StopIteration:
    break
