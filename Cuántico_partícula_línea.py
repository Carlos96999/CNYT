import Librería_vectores_matrices

def ProbabilidadPosicion(matriz, posicion):

    respuestaNum = Librería_vectores_matrices.NormaMatriz(matriz[posicion])**2
    respuestaDen = Librería_vectores_matrices.NormaMatriz(matriz)**2
    respuesta = respuestaNum/respuestaDen

    return respuesta

