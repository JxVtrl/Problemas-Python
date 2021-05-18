#    @jxvtrl    #

def alteraLista(lista):
    for altera in range(len(lista)):
        
        if isinstance(lista[altera], list):
            alteraLista(lista[altera])

        elif isinstance(lista[altera], int) == True:
            if lista[altera] %2 == 0:
                lista[altera] = lista[altera] + lista[altera]
            else:
                lista[altera] = lista[altera] * lista[altera]

        elif isinstance(lista[altera],str) == True:
            lista[altera] =  lista[altera].lower()

    return lista

print(alteraLista([1, 2, 3, 'pe-de-cabra', 5, 'a', 7]))