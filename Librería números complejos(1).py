from sys import stdin
import math
import random

def Fase(c1,c2):
    
    angulo1 = math.atan(c1[1]/c1[0])
    angulo2 = math.atan(c2[1]/c2[0])
    print("Fase")
    print(math.degrees(angulo1))
    print(math.degrees(angulo2))
    print()
    
def ConverCartePola(c1,c2):

    p1 = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
    p2 = (c2[0]*c2[0] + c2[1]*c2[1])**(1/2)
    print("Convertir cartesiano a polar")
    angulo1 = math.atan(c1[1]/c1[0])
    angulo2 = math.atan(c2[1]/c2[0])
    print("p = {0} angulo = {1}".format(p1,math.degrees(angulo1)))
    print("p = {0} angulo = {1}".format(p2,math.degrees(angulo2)))
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

        while c1[0] == 0 or c2[0] == 0:
            real = random.randrange(-40,40)
            c1[0] = real
            c12[0] = real
            
        Suma(c1,c2)
        Producto(c1,c2)
        Resta(c1,c2)
        Division(c1,c2)
        Modulo(c1,c2)
        Conjugado(c1,c2)
        ConverCartePola(c1,c2)
        Fase(c1,c2)
        print(c1,c2,"Estos son los complejos")
main()

