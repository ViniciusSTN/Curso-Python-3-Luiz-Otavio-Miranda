# copy -> cópia rasa (shallow copy)
# copia todos valores imutável, entretando valores mutávies apontarão para mesmo endereço de memória

# copy.deepcopy() -> cópia profunda (deep copy)

import copy 

d1 = {
  'c1',
  'c2',
}

# alterar um não afeta o outro
# shallow copy
d2 = d1.copy()

# alterar um não afeta o outro
# precisa importar copy
# deep copy
d3 = copy.deepcopy(d1)
