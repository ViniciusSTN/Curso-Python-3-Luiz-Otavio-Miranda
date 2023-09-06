# range -> tem fim
# count -> sem fim

from itertools import count

c1 = count(10, 4)
r1 = range(10)

print('c1', hasattr(c1, "__iter__")) # true
print('r1', hasattr(r1, "__iter__")) # true

print('c1', hasattr(c1, "__next__")) # true
print('r1', hasattr(r1, "__next__")) # false

for i in c1:
  if i >= 100:
    break
  print(i)

# count pode receber parâmetros
c2 = count(10, 4) # -> começa a partir do 10 e pula de 4 em 4 até o infinito
