#    @jxvtrl    #

num     = int(input("Informe um número: "))
Impares = []
Pares   = []

def Algarismos(numero) :
    if numero > 0:
        n = numero % 10
        if (n % 2) == 0:
            Pares.append(n)
        else:
            Impares.append(n)
        Algarismos(numero//10)
    
def multiplica(Impares):
    r = 1
    for x in Impares:
        r = r * x
    return r
Algarismos(num) 

if not Impares:
    print('n= {}'.format(num))
    print('f(n)= -1') 
else:
    print('Os numeros impares sao: {}'.format(Impares))
    print('n= {}'.format(num))
    resultado = multiplica(Impares)
    print('f(n)= {}'.format(resultado))
        