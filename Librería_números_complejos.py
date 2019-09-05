import math

def Fase(c1):
  
    if c1[0] != 0:
        angulo = math.atan2(c1[1],c1[0])
    else:
        print("No se puede dividir en cero",c1)

    return math.degrees(angulo)

def ConverPolaCarte(a,b):

    ParteReal = a*math.cos(b)
    ParteImagi = a*math.sin(b)

    return (ParteReal,ParteImagi)
    
def ConverCartePola(c1):
    
    if c1[0] != 0:
        p = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
        angulo = math.atan(c1[1]/c1[0])
    else:
        print("No se pede dividir entre cero",c1)

    return (p,math.degrees(angulo))
    
def Conjugado(complejo1):

    #complejo1[1] *= -1
    ParteReal = complejo1[0]
    ParteImagi = complejo1[1]
    #complejo1[1] *= -1

    return (ParteReal,-1*ParteImagi)
    
def Modulo(c1):

    modulo = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)

    return modulo
    
def Division(c1,c2):

    NumerReal = c1[0]*c2[0] + c1[1]*c2[1]
    DenomReal = c2[0]*c2[0] + c2[1]*c2[1]
    ParteReal = NumerReal/DenomReal
    NumerImagi = c2[0]*c1[1] - c1[0]*c2[1]
    DenomImagi = c2[0]*c2[0] + c2[1]*c2[1]
    ParteImagi = NumerImagi/DenomImagi
    
    return (ParteReal,ParteImagi)
    
def Resta(c1,c2):

    ParteReal = c1[0] - c2[0]
    ParteImagi = c1[1] - c2[1]
    return (ParteReal,ParteImagi)
    
def Producto(c1,c2):

    ParteReal = c1[0]*c2[0]-c1[1]*c2[1]
    ParteImagi = c1[0]*c2[1]+c1[1]*c2[0]

    return (ParteReal,ParteImagi)
    
def Suma(c1,c2):

    ParteReal = c1[0] + c2[0]
    ParteImagi = c1[1] + c2[1]

    return (ParteReal,ParteImagi)

def SumaVector(v1,v2):

    respuesta = []
    
    for i in range(len(v1)):
        respuesta.append(Suma(v1[i],v2[i]))
        

    return respuesta

def InversoVector(v):

    respuesta = []

    for i in range(len(v)):
        respuesta.append((v[i][0]*-1,v[i][1]*-1))

    return respuesta
        
def ProductoEscalarVector(c,v):

    respuesta = []

    for i in range(len(v)):
        respuesta.append(Producto(c,v[i]))

    return respuesta

def SumaMatriz(matriz1, matriz2):

    respuesta = []

    for i in range(len(matriz1)):
        respuesta.append(SumaVector(matriz1[i],matriz2[i]))

    return respuesta

def InversaMatriz(matriz):

    respuesta = []

    for i in range(len(matriz)):
        respuesta.append(InversoVector(matriz[i]))

    return respuesta

def ProductoEscalarMatriz(c,matriz):

    respuesta = []

    for i in range(len(matriz)):
        respuesta.append(ProductoEscalarVector(c,matriz[i]))
    
    return respuesta

def MatrizTranspuesta(matriz):

    respuesta = []
    
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        respuesta.append(fila)

    return respuesta

def MatrizConjugada(matriz):

    respuesta = []

    for i in range(len(matriz)):
        conjugado = []
        for j in range(len(matriz[i])):
            conjugado.append(Conjugado(matriz[i][j]))
        respuesta.append(conjugado)

    return respuesta

def MatrizAdjunta(matriz):

    respuesta = MatrizTranspuesta(matriz)
    respuesta = MatrizConjugada(respuesta)
    return respuesta

def NormaMatriz(matriz):

    respuesta = 0
    for i in (matriz):
        for j in i:
            respuesta += (j[0])**2
            respuesta += (j[1])**2

    return respuesta**0.5

def DistanciaMatriz(matriz1,matriz2):
    
    respuesta = 0
    
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            valor = Resta(matriz1[i][j],matriz2[i][j])
            respuesta += valor[0]**2 + valor[1]**2
    
    return respuesta**0.5

def MatrizUnitaria(filas,columnas):

    matriz = [[0 for i in range(columnas)]for j in range(filas)]
    uno = 0
    
    for i in range(filas):
        matriz[i][uno] = 1
        uno += 1

    print(matriz)
    
def RevisarUnitaria(matriz):

    matriz2 = MatrizTranspuesta(matriz)
    respuesta = []

    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(Producto(matriz[i][j],matriz2[i][j]))
        respuesta.append(fila)

    unitaria = MatrizUnitaria(len(matriz),len(matriz[0]))

    if respuesta == unitaria:
        return True
    else: return False
    
    
