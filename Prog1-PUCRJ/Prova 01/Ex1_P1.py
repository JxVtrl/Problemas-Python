#    @jxvtrl    #

def ValidarTamanho(x):
    while True:
        
        if len(x) < 3:
            x = input('A palavra deve conter no minimo 3 letras. Digite novamente: ')
        else:
            return x
        
def embaralha(s1, s2):
    p1 = s1[0:(len(s1) // 3)]
    p2 = s2[0]
    p3 = s1[-1]
    p4 = (s2[(len(s2) // 2):])[::-1]

    palavraToda = p1 + p2 + p3 + p4
    print(palavraToda)
  
s1 = input('Primeira palavra: ')
s1 = ValidarTamanho(s1) 
s2 = input('Segunda palavra: ')
s2 = ValidarTamanho(s2) 

embaralha(s1, s2)