#    @jxvtrl    #

import turtle

def AP(x1, y1, x2, y2):
    print('Perimetro=',(2*(x2-x1)+ 2*(y2-y1)))
    print('Area=',(x2-x1)*(y2-y1))
    return

def Desenho(x1, y1, x2, y2):
	
	Ed=turtle.Turtle()
	Ed.up()
	Ed.goto(x1,y1)
	Ed.down()
	Ed.fd(x2-x1)
	Ed.lt(90)
	Ed.fd(y2-y1)
	Ed.lt(90)
	Ed.fd(x2-x1)
	Ed.lt(90)
	Ed.fd(y2-y1)
	
	return    