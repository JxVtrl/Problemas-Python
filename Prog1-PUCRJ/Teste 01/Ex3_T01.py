#    @jxvtrl    #

def Senha():
	nome    = str(input('Insira seu nome utilizando CAPS:'))
	dia     = int(input('Dia do nascimento:'))
	mes     = int(input('Mes do nascimento:'))
	ano     = int(input('Ano do nascimento:'))

	print('Nome:',nome)
	print('Dia do nascimento:',dia)
	print('Mes do nascimento:',mes)
	print('Ano do nascimento:',ano)
	print('Sua Senha:',nome[3::-1],dia+mes+ano)
    
	return
