###
# 06 - Operadores y Expresiones
###


# 1. ¿QUÉ ES UN OPERADOR?
# Es un símbolo que le dice a Python que realice una operación concreta
# Los valores sobre los que actua se llaman operandos

# Operadores Aritméticos
# ----------------------
# suma: (+) -> 7 + 3 -> [Si alguno es float devuelve float]
# resta: (-) -> 7 - 3 -> [Si alguno es lfoat devuelve float]
# multiplicación: (*) -> 7 * 3 -> [Si alguno es float devuelve float]
# división: (/) -> 7 / 3 -> [Siempre devuelve float]
# división entera: (//) -> 7 // 3 -> [Si alguno es float devuelve float]
# módulo: (%) -> 7 % 3 -> [Si alguno es float devuelve float]
# potencia: (**) -> 7 ** 3

# Operadores comparación (Siempre devuelven un booleano: True/False)
# ----------------------
# igual a: (==) -> 5 == 5 -> True
# distinto de: (!=) -> 5 != 3 => True
# mayor que: (>) -> 5 > 3 -> True
# menor que: (<) -> 5 < 3 -> False
# mayor o igual que: (>=) 6 >= 6 -> True
# menor o igual que: (<=) 6 <= 3 -> False

# Vamos a ver un tipo de comparaciones especiales (strings)
# print("ana" == "Ana") -> False
# print("abc" < "abd") -> True
# print("B" < "a") -> True - Se comparan los valores unicodes a = 97, b = 66
# print("manzana" > "perla") -> False

# Operadores Lógicos (Combinan expresiones booleanas)
# ------------------
# Verdadero si ambos son verdaderos: (and) -> True and False (False)
# Verdadero si al menos uno es verdadero: (or) -> True or False (True)
# Invierte el valor booleano: (not) -> not True (False)

# Operadores de identidad (Comprueba si dos variables apuntan al mismo objeto)
# -----------------------
# si son el mismo objeto: (is) -> Devuelve True si son el mismo objeto
# si son objetos distintos: (is not) -> Devuelve True si son objetos distintos
# NOTA: (is/is not) -> comprueban si apuntan al mismo objeto
# NOTA: (==) -> comprueba si tienen el mismo valor

# Operadores de pertenencia (Comprueban si un valor está contenido en un secuancia)
# -------------------------
# el valor está en la secuencia: (in) -> True si está en la secuencia
# el valor no está en la secuencia: (not in) -> True si no está en la secuencia
# NOTA: una secuencia puede ser: string, lista, tupla, diccionario, etc
# Ejemplos:
# frase = "Python mola mucho"
# print("Python" in frase) -> Devuelve True
# print("java" in frase) -> Devuelve False
# print("mola" not in frase) -> Devuelve False

# 2. ¿QUÉ ES UNA EXPRESIÓN?
# Es una combinación de valores, variables y operadores que nos permite
# evaluarla y producir un resultado, veamos unos Ejemplo:

# 5 + 3 -> 8
# precio * 1.21 -> Precio con IVA
# edad >= 18 -> True/False
# nombre == "Ana" -> True/False
# x > 0 and x < 100 -> True/False
