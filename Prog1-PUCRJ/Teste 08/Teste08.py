#    @jxvtrl    #

def contaLetraEmIntervalo (lc,ltd):
    controle = 0

    for Achar_ltd in ltd:
        if type(Achar_ltd)==list:
            controle += contaLetraEmIntervalo(lc, Achar_ltd)

        elif type(Achar_ltd)==str:

            for letra_lc in lc:

                for letra_ltd in Achar_ltd:

                    if letra_lc==letra_ltd:
                        controle+=1

    return controle


lc = ['A', 'b', 'c']
ltd = ['xyb', [8, 5.0, False], 'A PUC-RIO fica no bairro', ['GAVEA', 'Zona Sul', 'RJ']] 

lc.append(input('Deseja adicionar algum elemento na lista lc? '))
print('A quantidade elementos da lista lc que aparece na lista ltd é de:', contaLetraEmIntervalo(lc, ltd))
contaLetraEmIntervalo(lc, ltd)