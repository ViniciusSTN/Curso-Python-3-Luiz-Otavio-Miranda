import sys

iterable = ['Eu', 'Tenho', '__iter__']

# itarator = iterable.__iter__() 
itarator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(10000)] # salva tudo na memoria -> fica pesado
generator = (n for n in range(10000)) # só salva quando iterar sobre o generator usando for (obs: não tem indice)

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
