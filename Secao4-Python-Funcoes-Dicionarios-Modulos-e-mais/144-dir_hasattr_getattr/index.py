# dir, hasattr e getattr em Python

# dir -> dentro do debug console -> dir(nome_da_variavel)

# hasattr() -> tem atributo ou método
# getattr() -> pega o método

string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)()) # pegar o método e executa
else:
    print('Não existe o método', metodo)
