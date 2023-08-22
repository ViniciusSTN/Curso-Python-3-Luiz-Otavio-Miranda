salas = [
  ['Maria', 'Helena'], # 0
  ['Elaine', ], # 1
  ['Luiz', 'João', 'Eduarda', (10, 20, 30)], # 2
#     0       1        2            3
]

print(salas[2][3][1])

for sala in salas:
  print(sala)
  for aluno in sala:
    print(aluno)
