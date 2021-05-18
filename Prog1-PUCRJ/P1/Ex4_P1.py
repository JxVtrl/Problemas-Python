#    @jxvtrl    #

def Cintura(c):
    if 79 <= c <= 86:
        return 'P'
    elif 87 <= c <= 92:
        return 'M'
    elif 93 <= c <= 108:
        return 'G'
    else:
        return 'ND'

def Quadril(q):
    if 97 <= q <= 104:
        return 'P'
    elif 105 <= q <= 116:
        return 'M'
    elif 117 <= q <= 126:
        return 'G'
    else:
        return 'ND'

def exibeTamanhoCalca(c,q,material):
    c1 = Cintura(c)
    q1 = Quadril(q)
    c2 = Cintura(c-4)
    q2 = Quadril(q-4)

    if material == 'jeans':
        if c1 == 'ND' or q1 =='ND':
            return 'Fora dos padroes de fabrica' 
        elif c1 > q1:
            return q1
        elif c1 < q1:
            return c1
    elif material == 'moleton':
        if c2 == 'ND' or q2 =='ND':
            return 'Fora dos padroes de fabrica' 
        elif c2 > q2:
            return q1
        elif c2 < q2:
            return c2

c = int(input('Qual é o tamanho da cintura? '))
q = int(input('Qual é o tamanho do quadril? '))
material = input('O material da calça será moleton ou jeans? ')

print(exibeTamanhoCalca(c,q,material)) 