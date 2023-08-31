# os modulos do python são singletons -> quando importa salva na memória, se importar novamente apontará para o mesmo módulo sem sofrer alteração

import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # agora é possivel fazer reload do módulo, se ele sofrer alteração no tempo de execução o reload irá atualizar
    print(i)

print('Fim')
