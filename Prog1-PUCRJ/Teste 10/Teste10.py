#    @jxvtrl    #

arq = open('B:\FACULDADE\Programacao\G2\T10\preferencias.txt','r')
lista = {}
rj    = []
rs    = []
sp    = []
ba    = []
sc    = []
x     = 0

for separa in arq:
    pos = separa[0:-1].split(';')
    c,e = pos[3], pos[1]

    if e not in lista:
        lista[e] = []
    if c not in lista[e]:
        lista[e].append(c)
for i in lista:
    print(i, ':', lista[i])
