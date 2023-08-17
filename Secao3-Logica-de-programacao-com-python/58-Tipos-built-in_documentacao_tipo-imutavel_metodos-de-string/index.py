# https://docs.python.org/pt-br/3/

# str, int, float, bool são imutáveis

string = 'vinicius santana'
outra_variavel = f'{string[:3]}ABC{string[4:]}' # para alterar algo, somente atribuindo a outra viariavel

# string[3] = 'abc'    # gera erro pois é imutável
print(outra_variavel.capitalize()) # somente primeira letra maiúscula
