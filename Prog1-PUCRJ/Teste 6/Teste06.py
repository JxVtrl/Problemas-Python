#    @jxvtrl    #

n = int(input("Escreva o numero de municipios: "))
c = T_recup = T_infect = 0

while c < n:
    nome        = input("Digite o nome do municipio: ").upper()
    infectados  = float(input("Numero de infectados: "))
    recuperados = float(input("Numero de recuperados: "))

    if recuperados > infectados:
        print('Não há dados estatisticos possiveis. ')
        continue

    porcentagem = (recuperados/infectados)*100

    print('=='*20) 
    print('Municipio: %s' % nome)
    print('Infectados: ', int(infectados))
    print('Recuperados: %.1f%%' % porcentagem)
    

   