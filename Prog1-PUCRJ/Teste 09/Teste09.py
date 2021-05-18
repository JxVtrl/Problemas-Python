#    @jxvtrl    #

import random 
import string

alfabeto = string.ascii_uppercase
vogais = ['a','e','i','o','u']
L1 = []

for inteiros in range(5):
    AcheInteiros = random.randint(65, 90)
    L1.insert(inteiros, AcheInteiros)

print('Questão um:')
print(L1)

for indice in range(len(L1)):
    if L1[indice] % 2 == 0 :
        L1[indice] = []

        for inteiros in range(5):
            L1[indice].insert(indice, random.choice(alfabeto))

print('\nQuestão dois:')
print(L1)

for i1 in range(len(L1)):
    valor = L1[i1]

    if type(valor) == list:

        for i2 in range(len(valor)):
            L1[i1][i2] = ord(valor[i2])
    else:
        L1[i1] = chr(valor)

print('\nQuestão tres:')
print(L1)

ContaVogal = 0

for i1 in range(len(L1)):
    valor = L1[i1]
    if type(valor) == list:
        for i1 in range(len(valor)):
            if chr(valor) in vogais:
                ContaVogal += 1
    

print('\nQuestão quatro:')
print('Quantidade de vogais: ' +str(ContaVogal))
 