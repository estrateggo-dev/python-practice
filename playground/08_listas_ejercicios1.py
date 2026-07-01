import os

os.system("clear")

"""
Ejercicio 01 - nivel básico

Enunciado:

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje
# "secreto".

Conceptos practicados:
- listas
- slicing
- concatenación

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

print(mensaje)
print(mensaje[7:])

"""
Ejercicio 02 - nivel básico

Enunciado:

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

Conceptos practicados:
- listas
- indices listas


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
numeros = [10, 20, 30, 40, 50]

print(numeros)

numeros[0], numeros[-1] = numeros[-1], numeros[0]

print(numeros)

"""
Ejercicio 03 - nivel básico

Enunciado:

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el
# pan de abajo, en ese orden.

Conceptos practicados:
- listas
- concatenacion

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print(sandwich)

"""
Ejercicio 04 - nivel básico

Enunciado:

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

Conceptos practicados:
- listas
- concatenación

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
lista = [1, 2, 3]
lista += lista

print(lista)

"""
Ejercicio 05 - nivel básico

Enunciado:

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra
# en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

Conceptos practicados:
- listas
- slicing


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
lista = [10, 20, 30, 40, 50]

centro = len(lista) // 2

print(lista[centro])


"""
Ejercicio 06 - nivel básico

Enunciado:

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y
# concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

Conceptos practicados:
- listas
- revertir elementos listas
- slicing
- concatenación

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista) // 2

lista_invertida = lista[:mitad][::-1] + lista[mitad:]
