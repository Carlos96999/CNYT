import Librería_vectores_matrices

def Canicas(matriz, vector, click):

    if len(matriz) == len(vector):

        respuesta = vector
        while click != 0:
            
            respuesta = Librería_vectores_matrices.AccionMatrizVector(matriz,respuesta)
            click -= 1

        return respuesta

##        for i in range(len(respuesta)):
##
##            if respuesta[i][0] != 0:
##                respuesta[i][0] = True
##                respuesta[i][1] = True
##            else:
##                respuesta[i][0] = False
##                respuesta[i][1] = False
    else:
        print("Dimensiones incorrectas. Por favor digita de nuevo")

def Probabilidad(matriz, vector):

    respuesta = vector
    
    if len(matriz) == len(vector):        
        respuesta = Librería_vectores_matrices.AccionMatrizVector(matriz,respuesta)
        return respuesta
    else:
        print("Dimensiones incorrectas. Por favor digita de nuevo")

def DobleRendija(matriz):

    respuesta = matrizmultiplication(matriz,matriz)
    return respuesta

