lista = [
  'a', 1, 1.1, True, [0, 1, 2], (1, 2),
  {0, 1}, {'nome': 'Vinicius'},
]

for item in lista:
  if isinstance(item, set):
    item.add(5)
    print(item, isinstance(item, set))

# isinstance(item, str)
# isinstance(item, int)
# isinstance(item, float)
# ...
