#    @jxvtrl    #

def imprime(v):
	v=int(v)
	print('Valor: R$', v)
	print('Qtd. de celulas:')
	print(v//50, 'cedulas de 50')
	print((v%50)//20, 'cedulas de 20')
	print(((v%50)%20)//2, 'cedulas de 2')
	print((((v%50)%20)%2)//1, 'cedulas de 1')

	return