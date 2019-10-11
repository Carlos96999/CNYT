import Librería_vectores_matrices

def ProbabilidadPosicion(matriz, posicion):

    respuestaNum = Librería_vectores_matrices.NormaMatriz(matriz[posicion])**2
    respuestaDen = Librería_vectores_matrices.NormaMatriz(matriz)**2
    respuesta = respuestaNum/respuestaDen

    return respuesta

def AmplitudTransicional(matriz1, matriz2):
    respuesta = Librería_vectores_matrices.matrizmultiplication(matriz1,Librería_vectores_matrices.MatrizTranspuesta(Librería_vectores_matrices.MatrizConjugada(matriz2)[0]))
    parteReal = 0
    parteImagin = 0

    for i in range(len(respuesta)):
        parteReal += respuesta[0][0][0]
        parteImagin += respuesta[0][0][1]

    return (parteReal,ParteImagin)
