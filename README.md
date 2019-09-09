# Calculadora de números complejos
Este programa muestra el resultado de unas operaciones realizadas con números complejos las cuales son:
  - Suma                           - Conjugado
  - Resta                          - Conversión cartesiano a polar
  - Producto                       - Conversión polar a cartesiano
  - División                       - Fase
  - Modulo.
  
También fueron agregadas operaciones entre vectores y matrices:
  - Suma de vectores                                        - Matriz adjunta
  - Inverso de un vector                                    - Acción de una matriz sobre un vector
  - Producto de un escalar por un vector                    - Norma de una matriz
  - Suma de matrices                                        - Distancia de una matriz
  - Inversa de una matriz                                   - Matriz unitaria
  - Producto de un escalar por una matriz                   - Matriz hermitania
  - Matriz transpuesta                                      - Producto tensor
  - Matriz conjugada

# Instalación
Debes tener instalado el programa ****python**** en su última versión para poder hacer uso de la librería. Puedes descargarlo del siguiente enlace https://www.python.org/downloads/; al descargarlo vuelves a este enlace y clonas el repositorio, lo abres con el editor de python y ahí puedes empezar a realizar tus pruebas correspondientes.



# Ejecutando las pruebas
 1. Abrir con el editor de python los archivos con nombre terminado en ****unit test****. 
 2. Ingresar los datos a probar; la estructura para las pruebas unitarias es la siguiente:
  self.assertEqual(Librería_números_complejos.Función de la cual deseas realizar la prueba(parametro 1, parametro2),          respuesta que debería dar la operación).
 3. Ejecutar el programa, si la respuesta estuvo escrita correctamente el programa mostrará un ok con el tiempo que duró la ejecución.



# Análisis de pruebas
El uso de esta librería te puede ayudar a rectificar operaciones entre complejos ya sea para estudio o solo conocimiento. Al hacer el uso de las fórmulas correctas hay una completa confianza sobre el resultado.
\n
Para hacer uso de las pruebas de unidad debes seguir los siguientes pasos:
 1. 
# Operaciones
 Las operaciones de elementos complejos se realiza con las siguientes formulas:
 ****Los números complejos están identificados como c1 y c2, el cual es una tupla de la siguiente forma (parte real, parte imaginaría) la parte real como [0] y la imaginaría [1]****
 ****Los vectores complejos están identificados como v1 y v2****
 
 # Suma 
   ParteReal = c1[0] + c2[0]
   ParteImagi = c1[1] + c2[1]
  
  
 # Resta
   ParteReal = c1[0] - c2[0]
   ParteImagi = c1[1] - c2[1]
  
 # División
   NumerReal = c1[0]*c2[0] + c1[1]*c2[1]
   DenomReal = c2[0]*c2[0] + c2[1]*c2[1]
  
   NumerImagi = c2[0]*c1[1] - c1[0]*c2[1]
   DenomImagi = c2[0]*c2[0] + c2[1]*c2[1]
 
 # Multiplicación
   ParteReal = c1[0]*c2[0]-c1[1]*c2[1]
   ParteImagi = c1[0]*c2[1]+c1[1]*c2[0]
  
 # Módulo
   modulo = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
  
 # Conjugado
   ParteReal = complejo1[0]
   ParteImagi = complejo1[1]*-1 
 
 # Conversión de cartesiano a polar
   p = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
   angulo = math.atan(c1[1]/c1[0])
 
 # Conversión de polar a cartesiano
   ParteReal = a*math.cos(b)
   ParteImagi = a*math.sin(b)
  
 # Fase
   angulo = math.atan2(c1[1],c1[0])

 # Matriz transpuesta
   matriz<sub>i,j</sub> = matriz<sub>j,i</sub>
 
 # Norma de una matriz
   respuesta += (j[0])^2
   respuesta += (j[1])^2
   
 
 
 
 
 # Autor: Carlos Amorocho
 
 
 
