###
# 08 - Listas
###

# Las listas son secuencias mutables de elementos, pueden contener elementos
# de diferentes tipos, basicamente e sun conjunto de elenmentos.

import os

os.system("clear")

# Creación de listas
# ------------------
lista1 = [1, 2, 3, 4, 5]  # lista de enteros
lista2 = ["manzana", "peras", "uvas", "naranjas"]  # lista de cadenas de texto
lista3 = [1, "avión", 3.1415, False]  # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2, 2, 5], ["avion", "coche", "motocicleta"]]
matrices = [[1, 2], [3, 6], [4, 3]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrices)

# Acceder e elementos por índices
# --------------------------------
# En programación el primer índice de una lista es el elemento 0
print(lista2[0])

# Para acceder al último elemento se hace a través del elemento -1
print(lista2[-1])

# Cómo acceder a un elemento de una lista de listas (matrices)
# matrices([Se accede al par][se accede al elemento del par (0,1,2,...)])

print(matrices[1][1])  # Muestre el número 6
print(matrices[0][0])  # Muestra el número 1
print(lista_de_listas[1][2])  # Muestra "motocicleta"

# Slicing en Python (rebando)
# -----------------
# El slicing lo que hacer es poder rescatar varios elementos de una lista
# print(lista[indice1:indice2]) -> Desde el índice1 hasta el inicio del indice2 (no lo incluye)  # noqa: E501
# NOTA -> El primer índice está INCLUIDO, el segundo índice NO ESTA INCLUIDO
# lista[desde:hasta]

print(lista1[0:2])  # Devuele los elementos desde el índice [0, 2)

print(lista1[:3])  # Devuelve los tres primero elementos desde el principio

print(lista1[:])  # Realiza una copia completa de la lista

# Parámetro PASO dentro del slicing
# lista[desde:hasta:paso]
# Por defecto estos parámetros son desde: inicio // hasta: final // paso: de 1 en 1

lista4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista4[::2])  # Hace una copia pero de 2 en 2 [1, 3, 5, 7]

print(lista4[::-1])  # Devuelve una copia de la lista pero con los elementos invertidos

# MODIFICAR elementos de una lista
# --------------------------------
lista4[0] = 20
print(lista4)

# Al intentar modificar un elemento de la lista que no existe, Python lanzara una error
# Si una lista tiene 5 índices y queremos acceder al índice 6, lanza error por consola

# AÑADIR elementos a una lista
# ----------------------------
# Vamos a ver dos maneras de hacerlo (segunda es mejor)

lista5 = [1, 2, 3, 4]

# 1 - fomra larga y menos eficiente
lista5 = lista5 + [5, 5, 5]
print(lista5)  # [1, 2, 3, 4, 5, 5, 5] El signo (+) concatena elementos a la lista

# 2 - forma corta y más eficiente
lista5 += [0, 0]
print(lista5)  # [1, 2, 3, 4, 5, 5, 5, 0, 0]

# LONGITUD de una lista
# ---------------------
print(f"Longitud de la lista 5: {len(lista5)}")

# También podemos contar cuantos veces aparece un elemento repetido en una lista
listado = ["a", "t", "u", "t", "s", "e", "t"]
print(listado.count("t"))  # 3

# -------------------------------
# MÉTODOS asociados a las listas
# ------------------------------

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# MÉTODOS AÑADIR - INSERTAR ELEMENTOS
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

# Añadir UN elemento al final de una lista:
lista5.append(99)
print(lista5)  # [1, 2, 3, 4, 5, 5, 5, 0, 0, 99]

nombres = ["carlos", "juan", "ana", "pedro"]
nombres.append("ramon")
print(nombres)  # ['carlos', 'juan', 'ana', 'pedro', 'ramon']

variado = [1, "arbol", "casa", 3.14]
variado.append("soldado")
print(variado)  # [1, 'arbol', 'casa', 3.14, 'soldado']

# Insertar un elemento en un posición concreta de la lista:
# insert(indice, elemento)
ciudades = ["madrid", "sevilla", "barcelona", "cadiz"]
ciudades.insert(1, "malaga")
print(ciudades)  # ['madrid', 'malaga', 'sevilla', 'barcelona', 'cadiz']

# Añadir varios elementos al final de la lista
notas = [3, 5, 8, 4, 9]
notas.extend([3, 5, 0])
print(notas)  # [3, 5, 8, 4, 9, 3, 5, 0]

# xxxxxxxxxxxxxxxxxxxxxxxxx #
# MÉTODOS ELIMINAR ELEMENTOS
# xxxxxxxxxxxxxxxxxxxxxxxxx #

# Eliminar un elemento de una lista
# Elimina la PRIMERA coincidencia dentro de la lista del elemento que le hemos pasado
cantidades = [100, 200, 300, 400]
cantidades.remove(200)
print(cantidades)  # [100, 300, 400]

# Eliminar un índice concreto de una lista
# pop() por defecto elimina el último de la lista
# po(0) elimina el índice 0 de la lista
letras = ["a", "b", "c"]
letras.pop(0)

# Eliminar todos los elementos de la lista
letras.clear()
print(letras)  # []

# Eliminar un rango de elementos (sintaxis de slicing)
iconos = ["🚒", "🛵", "☂️", "💻", "🍳"]
del iconos[3:]
print(iconos)  # ['🚒', '🛵', '☂️']

# xxxxxxxxxxxxxxxxxxxxxxx #
# MÉTODOS ORDENAR LISTAS
# xxxxxxxxxxxxxxxxxxxxxxx #

# Ordena una lista modificando la original
# lista.sort()
numbers = [3, 0, 12, 9, 6]
numbers.sort()
print(numbers)  # [0, 3, 6, 9, 12]

personas = ["ana", "Jose", "beatriz", "pedro", "Pedro"]
personas.sort()
print(personas)  # ['Jose', 'Pedro', 'ana', 'beatriz', 'pedro'] OJO CON  LAS MAYÚSCULAS

personas_b = ["ana", "Jose", "beatriz", "pedro", "Pedro"]
personas_b.sort(
    key=str.lower
)  # La llave le dice que quiere que las compare todas minúsculas
print(personas_b)  # ['ana', 'beatriz', 'Jose', 'pedro', 'Pedro']

# Ordena una lista creando una copia (una nueva lista)
# sorted(lista) -> Retorna una lista nueva, podemos guardarla en unba variable

calificaciones = [3.5, 0.5, 9.8, 6.4, 5.1, 2.75]
nuevas_calificaciones = sorted(calificaciones)
print(calificaciones)  # [3.5, 0.5, 9.8, 6.4, 5.1, 2.75]
print(nuevas_calificaciones)  # [0.5, 2.75, 3.5, 5.1, 6.4, 9.8]

frutas = ["manzana", "pera", "limón", "naranja", "uva"]
sorted_frutas = sorted(frutas)
print(frutas)  # ['manzana', 'pera', 'limón', 'naranja', 'uva']
print(sorted_frutas)  # ['limón', 'manzana', 'naranja', 'pera', 'uva']
