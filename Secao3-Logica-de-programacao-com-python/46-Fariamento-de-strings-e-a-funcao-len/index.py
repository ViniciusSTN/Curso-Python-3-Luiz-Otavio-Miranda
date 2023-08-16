"""
Fatiamento de strings

 012345678
 ola mundo
-987654321

Fatiamento [i:f:p] [::]
Obs: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:]) # fatiar a partir do 4
print(variavel[4:7]) # do 4 ao 6
print(variavel[:5]) # do 0 ao 4
print(variavel[-8:-2])
print(len(variavel)) # 9 caracteres
print(variavel[0:9:2]) # o terceiro indice é o passo
print(variavel[::-1]) # passo invertido, nesse caso inverte a string

array = [1,2,3,4,5,6,7,8,9,10]
print(array[::-1]) # inverte os indices do array
print(array[2:]) # fatia o array a partir do indice informado

