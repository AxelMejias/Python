#Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y 
#arrays 

print("La librería NumPy es una de las bibliotecas más importantes y ampliamente utilizadas en Python"
    " para trabajar con matrices y arrays. Proporciona soporte para arrays y matrices de gran tamaño,"
    " así como una colección de funciones matemáticas para operar sobre estos arrays. NumPy es fundamental"
    " para el análisis de datos, la ciencia de datos y la computación científica")

#"pip install numpy" utilizaremos para instalar NumPy en nuestro PC desde cmd
#podemos verificar que NumPy está instalado usando el codigo [ print(np.__version__) ]

import numpy as np

# Crear un array unidimensional
array_1d = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:", array_1d)

# Crear un array bidimensional (matriz)
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array bidimensional:\n", array_2d)

# Crear un array de ceros
array_zeros = np.zeros((3, 3))
print("Array de ceros:\n", array_zeros)

# Crear un array de unos
array_ones = np.ones((2, 2))
print("Array de unos:\n", array_ones)

# Crear un array de números aleatorios
array_random = np.random.rand(3, 3)
print("Array de números aleatorios:\n", array_random)

# Suma de arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
suma = array_a + array_b
print("Suma de arrays:", suma)

# Multiplicación de arrays
multiplicacion = array_a * array_b
print("Multiplicación de arrays:", multiplicacion)

# Suma de todos los elementos de un array
suma_total = np.sum(array_a)
print("Suma de todos los elementos:", suma_total)

# Media de los elementos de un array
media = np.mean(array_a)
print("Media de los elementos:", media)