x = 1

def escopo():
  global x # manipula o x global
  x = 10
  print(x)

escopo()
print(x)
