#    @jxvtrl    #

def mereceDesconto(meia, inteira, hora):
    if (meia + inteira) > hora:
        return True
    else:
        return False

hora        = input("Horario da compra do ingresso? (hh:mm) ")
hora        = int(hora[0:2])
preco       = float(input("Digite o preço do ingresso: "))

qtd_int     = int(input("Quantidade de ingressos inteiros? " ))
qtd_meia    = int(input("Quantidade de ingressos meia entrada? "))

qtd = (qtd_int + qtd_meia)
valor = ((qtd_int * preco)+ (qtd_meia * (preco/2)))
valor_Desconto = 0

print("O valor total sera: %.2f" %valor)

if mereceDesconto (qtd_meia, qtd_int, hora):
    if qtd > 5 and qtd == qtd_int:
        valor_Desconto = valor*0.6
       
    elif  qtd > 5 and qtd == qtd_int + qtd_meia:
        valor_Desconto = valor*0.7  
        
    elif  qtd > 5 and qtd ==  qtd_meia:
        valor_Desconto = valor*0.75  

    elif  qtd < 5 : 
        valor_Desconto = valor*0.8 

if valor_Desconto > 0:
    print("Valor descontado: %.2f"%(valor-valor_Desconto))
    print("Valor com Desconto: %.2f" %valor_Desconto)
