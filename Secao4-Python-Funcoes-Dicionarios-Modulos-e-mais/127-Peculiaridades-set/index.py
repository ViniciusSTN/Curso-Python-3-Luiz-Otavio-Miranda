# eficientes para remover valores duplicaods de iteráveis
# valores mutáveis não podem ser adicionados (apenas tuplas podem)
# não garante a order
# não tem índice mas é possível iterar

s1 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s1) # {1, 2, 3}

l1 = [1,2,3,3,3,3,2,1,5,6]
s2 = set(l1) # remove repetidos pois foi convertido para set
l2 = list(s2) # volta a ser list
print(l2)

# OBS: não pode ter tipos mutáveis dentro, pois da erro
# OBS2: a tupla pode
# s3 = {1, 2, 3, 3, [123]} # gera erro
s3 = {1, 2, 3, 3, (123456,)} # não gera erro

print(3 in s3) # True
print(3 not in s3) # False

for sla in s3:
  print(sla) # (123456,)
