## Declaração de autoria: Declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa. 
## Matricula: 2011530
## Nome: Joao Vinicius Vitral

def replica(s, c = False):
    v = ("a", "e", "i", "o", "u")
    p = []

    if c == False:
        x = len(s)-1
        Ponto = False

        while x >= 0:
            if s[x] == ".":
                Ponto = True
                p.append(s[x])
                corta = s[0:x]
                p = p + replica(corta, True)

                break
            else:
                p.append(s[x])

            x = x - 1

        if Ponto:
            return "".join(p[::-1]) 
        else:
            return "String Vazia"
            
    else:
        x = 0

        while x < len(s): 
            p.append(s[x])

            if s[x] in v:
                p.append(s[x]*2)
                
            x = x + 1
        return p[::-1]

p = input("Escreva duas palavras separadas por '.': ")
p = replica(p)
print("A nova string é: {}".format(p))