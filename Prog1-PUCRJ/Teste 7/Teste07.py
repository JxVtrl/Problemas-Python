#    @jxvtrl    #

def quadradoPerfeito(a,b): 
    for controle in range(a,b):
        if(b - controle >= 4):

            print((controle * (controle+1) * (controle+2) * (controle+3)) + 1)

a = int(input('Qual é o primeiro numero?'))
b = int(input('Qual é o segundo numero?')) + 1

quadradoPerfeito(a,b)