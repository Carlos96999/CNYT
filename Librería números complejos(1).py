from sys import stdin
import math
import random

def Fase(c1,c2):

    print("Fase")
    
    if c1[0] != 0:
        angulo1 = math.atan(c1[1]/c1[0])
        print(math.degrees(angulo1))
    else:
        print("No se puede dividir en cero",c1)
    if c2[0] != 0:
        angulo2 = math.atan(c2[1]/c2[0])
        print(math.degrees(angulo2))
    else:
        print("No se puede dividir en cero",c2)    
    print()

def ConverPolaCarte(a,b):

    print("Convertir polar a cartesiano")

    ParteReal = a*math.cos(b)
    ParteImagi = a*math.sin(b)
    Imprimir(ParteReal,ParteImagi)

    
def ConverCartePola(c1,c2):

    print("Convertir cartesiano a polar")
    
    if c1[0] != 0:
        p1 = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
        angulo1 = math.atan(c1[1]/c1[0])
        print("p = {0} angulo = {1}".format(p1,math.degrees(angulo1)))
    else:
        print("No se pede dividir entre cero",c1)
    if c2[0] != 0:
        p2 = (c2[0]*c2[0] + c2[1]*c2[1])**(1/2)
        angulo2 = math.atan(c2[1]/c2[0])
        print("p = {0} angulo = {1}".format(p2,math.degrees(angulo2)))
    else:
        print("No se puede dividir entre cero",c2)
    print()
    
def Conjugado(complejo1,complejo2):

    complejo1[1] *= -1
    complejo2[1] *= -1
    print("Conjugado")
    ParteReal = complejo1[0]
    ParteImagi = complejo1[1]
    Imprimir(ParteReal,ParteImagi)
    ParteReal = complejo1[0]
    ParteImagi = complejo1[1]
    Imprimir(ParteReal,ParteImagi)
    complejo1[1] *= -1
    complejo2[1] *= -1
    
def Modulo(c1,c2):

    modulo1 = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
    modulo2 = (c2[0]*c2[0] + c2[1]*c2[1])**(1/2)
    print("Modulo")
    print(modulo1)
    print(modulo2)
    print()
    
def Division(c1,c2):

    NumerReal = c1[0]*c2[0] + c1[1]*c2[1]
    DenomReal = c2[0]*c2[0] + c2[1]*c2[1]
    ParteReal = NumerReal/DenomReal
    NumerImagi = c2[0]*c1[1] - c1[0]*c2[1]
    DenomImagi = c2[0]*c2[0] + c2[1]*c2[1]
    ParteImagi = NumerImagi/DenomImagi
    print("División")
    Imprimir(ParteReal,ParteImagi)
    
def Resta(c1,c2):

    ParteReal = c1[0] - c2[0]
    ParteImagi = c1[1] - c2[1]
    print("Resta")
    Imprimir(ParteReal,ParteImagi)
    
def Producto(c1,c2):

    ParteReal = c1[0]*c2[0]
    ParteImagi = c1[0]*c2[1]+c1[1]*c2[0]+c1[1]*c2[1]
    print("Producto")
    Imprimir(ParteReal,ParteImagi)
    
def Suma(c1,c2):

    ParteReal = c1[0] + c2[0]
    ParteImagi = c1[1] + c2[1]
    print("Suma")
    Imprimir(ParteReal,ParteImagi)

def Imprimir(ParteReal,ParteImagi):
    if ParteReal >= 0 and ParteImagi >= 0:
        print("C = {0} + {1}i".format(ParteReal,ParteImagi))
    elif ParteReal < 0 and ParteImagi >= 0:
        print("C = -{0} + {1}i".format(ParteReal*-1,ParteImagi))
    elif ParteReal < 0 and ParteImagi < 0:
        print("C = -{0} - {1}i".format(ParteReal*-1,ParteImagi*-1))
    else:
        print("C = {0} - {1}i".format(ParteReal,ParteImagi*-1))
    print()
          
    
def main():

    for i in range(8):
        real = random.randrange(-40,40)
        imaginario = random.randrange(-40,40)
        c1 = [real,imaginario]
        real = random.randrange(-40,40)
        imaginario = random.randrange(-40,40)
        c2 = [real,imaginario]
            
        Suma(c1,c2)
        Producto(c1,c2)
        Resta(c1,c2)
        Division(c1,c2)
        Modulo(c1,c2)
        Conjugado(c1,c2)
        ConverCartePola(c1,c2)
        r = random.randrange(-40,40)
        angulo = random.randrange(-40,40)
        ConverPolaCarte(r,angulo)
        Fase(c1,c2)
        print(c1,c2,"Estos son los complejos")
main()

