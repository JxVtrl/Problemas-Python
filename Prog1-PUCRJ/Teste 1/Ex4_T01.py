#    @jxvtrl    #

def Senha():
    nome    = str(input('Insira seu nome utilizando CAPS: '))
    dd      = int(input('Dia do nascimento: '))
    mm      = int(input('Mes do nascimento: '))
    aa      = int(input('Ano do nascimento: '))

    print('Nome:',nome)
    print('Dia do nascimento:',dd)
    print('Mes do nascimento:',mm)
    print('Ano do nascimento:',aa)

    num     = dd+mm+aa
    num     = str(num)

    print('Senha Gerada:',nome[3::-1]+num)

    return