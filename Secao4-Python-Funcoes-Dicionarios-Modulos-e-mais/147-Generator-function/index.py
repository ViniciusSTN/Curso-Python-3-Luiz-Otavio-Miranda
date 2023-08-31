def generator():
  yield 1 # pausa e espera chamar next
  print("continuando")
  yield 2 # pausa e espera chamar next
  print("continuando")
  yield 3 # pausa e espera chamar next
  return 'Acabou'

# na primeira execução é so para definir o corpo da função e pausar no primeiro yield
gen = generator() # gera um generator

for n in gen:
  print(n)



def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(maximum=10)
for n in gen:
    print(n)
