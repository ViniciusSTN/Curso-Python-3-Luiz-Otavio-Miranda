iterable = ['Eu', 'Tenho', '__iter__']

# itarator = iterable.__iter__() 
itarator = iter(iterable) # tem __iter__ e __next__

print(next(itarator))
print(next(itarator))
print(next(itarator))
print(next(itarator)) # exceção -> StopIteration
