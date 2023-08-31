# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else: # else não é muito usado, faz a mesma coisa que finally
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
