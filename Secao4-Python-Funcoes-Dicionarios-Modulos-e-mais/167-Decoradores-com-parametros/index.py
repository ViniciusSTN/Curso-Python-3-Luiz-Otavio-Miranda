# exemplos de uso de decoradores:

# Registro de Log: Você pode usar decoradores para registrar informações de log, como a hora de execução de uma função, os argumentos que foram passados para ela e o resultado retornado.

# Autenticação e Autorização: Decoradores podem ser usados para verificar se um usuário tem permissão para acessar uma determinada função ou recurso.

# Medição de Desempenho: Você pode usar decoradores para medir o tempo de execução de uma função e fazer análises de desempenho.

# Validação de Entrada: Decoradores podem ser usados para verificar se os argumentos passados para uma função são válidos.


# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
