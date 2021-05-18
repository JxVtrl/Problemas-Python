#    @jxvtrl    #

import math

def distEntre2Pontos (xA, yA, xB, yB):
    distancia = (math.sqrt((xA - xB)**2 + (yA - yB)**2))
    print(distancia)
    return distancia

def compararetas(xA, yA, xB, yB, xC, yC):
    distEntre2Pontos(xB, yB, xC, yC) > distEntre2Pontos(xA, yA, xC, yC)
    return 
    
xA = int(input('Digite o X da coordenada A: '))
yA = int(input('Digite o Y da coordenada A: '))
xB = int(input('Digite o X da coordenada B: '))
yB = int(input('Digite o Y da coordenada B: '))

pontoA = ('({},{})'.format(xA,yA)) 
pontoB = ('({},{})'.format(xB,yB)) 


if compararetas(xA, yA, xB, yB, 0, 0) == True:
    print('O ponto A {} está mais perto da origem. '.format(pontoA))
else:
    print('O ponto B {} está mais perto da origem. '.format(pontoB))