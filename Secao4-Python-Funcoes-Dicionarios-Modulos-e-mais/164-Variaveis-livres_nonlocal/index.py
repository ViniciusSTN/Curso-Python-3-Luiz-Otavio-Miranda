# variaveis livres + nonlocal (locals, globals)

print(globals()) # mostra as variaveis globais

def fora(x):
    a = x # varival livre (free var)

    def dentro():
        # print(locals()) # mostra as variaveis locais no bloco

        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

# ------------------------------------------------------------------

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # informa que essa variável não é local, eleva o escopo para buscar o variavel
        nonlocal valor_final # se não tivesse isso daria erro (comentar para ver)
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
