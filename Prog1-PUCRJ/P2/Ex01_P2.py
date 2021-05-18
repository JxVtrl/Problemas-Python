#    @jxvtrl    #

arq = open('B:\FACULDADE\Programacao\G2\P2\Q1\paciente.txt','r')
lista = {}

for contaPacientesMedicos in arq:
    pos = contaPacientesMedicos[0:-1].split(',')
    c,e = pos[0],pos[2]
    controle = 0

    if e not in lista:
        lista[e] = []

    if c not in lista[e]:
        lista[e].append(c)

for i in lista:
    print(i, ':', len(lista[i]))