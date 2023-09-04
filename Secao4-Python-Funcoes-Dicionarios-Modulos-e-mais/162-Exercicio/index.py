# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    # closure
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5) # salva o 5 na memória da função
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10)) # x já está salvo na memória, basta passar o y
print(multiplica_por_dez(10))
