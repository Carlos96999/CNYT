import Librería_vectores_matrices

def Canicas(matriz, vector):

    if len(matriz) == len(vector):
        respuesta = Librería_vectores_matrices.AccionMatrizVector(matriz,vector)

        for i in range(len(respuesta)):

            if respuesta[i][0] != 0:
                respuesta[i][0] = True
                respuesta[i][1] = True
            else:
                respuesta[i][0] = False
                respuesta[i][1] = False
    else:
        print("Dimensiones incorrectas. Por favor digita de nuevo")


