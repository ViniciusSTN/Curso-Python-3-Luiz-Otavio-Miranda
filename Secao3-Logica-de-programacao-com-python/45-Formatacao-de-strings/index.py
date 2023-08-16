"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
> - esquerda
< - direita
^ - centro
= - Forçar o sinal a aparcer antes dos zeros
sinal -> + ou -
ex: 0>-100,.1f
conversion flags - !r !s !a   sla bixo
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:%^10}.')
print(f'{-1000.97897845702:+,.1f}.') # o sinal + mostra sempre o sinal quando for positivo ou negativo
print(f'{1000.97897845702:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!a}')
