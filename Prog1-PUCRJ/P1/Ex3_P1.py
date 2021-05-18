#    @jxvtrl    #

def trocaVogaisConsecutivas(Achaletra):
    if len(Achaletra) == 1:

        return Achaletra

    vogais = 'a', 'e', 'i', 'o', 'u'

    if Achaletra[-1] in vogais and Achaletra[-2] in vogais:

        return trocaVogaisConsecutivas(Achaletra[:-2]) + '*'

    else:

        return trocaVogaisConsecutivas(Achaletra[:-1]) + Achaletra[-1]

Achaletra = input('Insira uma palavra: ')
print(trocaVogaisConsecutivas(Achaletra))  