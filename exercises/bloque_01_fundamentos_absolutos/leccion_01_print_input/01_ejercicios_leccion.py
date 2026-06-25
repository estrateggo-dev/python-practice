"""
Ejercicio 01 - nivel básico

Enunciado:
Crea un archivo que imprima exactamente las siguientes líneas:

¡Hola, mundo!
Estoy aprendiendo python
Esto mola

Conceptos practicados:
- print()



Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print("¡hola, mundo!")
print("Estoy aprendiendo Python")
print("Esto mola\n")

"""
Ejercicio 02 - nivel básico

Enunciado:
Unsando una sola llamada a print() con el parametro sep, produzca la salida:
2024/01/15

Conceptos practicados:
- print()
- sep


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print("2024", "01", "15\n", sep="/")

"""
Ejercicio 03 - nivel básico

Enunciado:
Usndo el parámetro end, haz que estas tres llamadas a print() aparezcan en la misma
línea sepadas por -

Conceptos practicados:
- print()
- end


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print("Python", end=" - ")
print("es", end=" - ")
print("genial\n")

"""
Ejercicio 04 - nivel básico

Enunciado:
Pide al usuario que introduzca su nombre y salúdale con un mensaje personalizado:

¿Cuál es tu nombre? María
¡Hola, María! Bienvenida a Python.

Conceptos practicados:
- input()
- print()


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre = input("¿Cúal es tu nombre?: ")
print(f"¡Hola, {nombre}! Bienvenida a Python\n")

"""
Ejercicio 05 - nivel intermedio

Enunciado:
Pide al usuario su nombre y ciudad, y muestra una tarjeta de presentación formateada:

¿Tu nombre? Carlos
¿Tu ciudad? Sevilla

=========================

    Nombre : Carlos

    Ciudad : Sevilla

=========================

Conceptos practicados:
- input()
- print()
- formateo

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre = input("¿Cúal es tu nombre?: ")
ciudad = input("¿Cúal es tu ciudad?: ")

print(f"\n{'=' * 30}\n\n\tNombre : {nombre}\n\n\tCiudad : {ciudad}\n\n{'=' * 30}\n")

"""
Ejercicio 06 - nivel intermedio

Enunciado:
Pide dos número al usuario (como float) y muestra las cuatro operaciones básicas
formateadas: suma, resta, producto y división

Conceptos practicados:
- input
- print
- casting

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
num1 = float(input("Introduzca el numero 1: "))
num2 = float(input("Introduzca el número 2: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2

print(
    f"\nSuma\t\t: {suma}\n"
    f"Resta\t\t: {resta}\n"
    f"Producto\t: {producto}\n"
    f"División\t: {division}\n"
)

"""
Ejercicio 07 - nivel intermedio

Enunciado:
crea un prograna que pida el nombre de un producto y su precio, y muestre
el precio con IVA (21%)

Conceptos practicados:
- input()
- print
- casting

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre_producto = input("¿Qué producto quiere comprar? : ")
precio_producto = float(input("¿Precio sin IVA del producto : "))

print(f"\n{'-' * 40}\n")
print(
    f"Producto\t: {nombre_producto}\n"
    f"Precio\t\t: {precio_producto} €\n"
    f"IVA (21%)\t: {precio_producto * 0.21} €\n"
    f"Total\t\t: {(precio_producto * 1.21):.2f} €\n"
)


"""
Ejercicio 08 - nivel avanzado

Enunciado:
Sin usar variables intermedias (todo en los print()), pide el nombre del usuario y
muestra el patrón donde N es la longitus de su nombre:

Ejemplo -> ¿Tu nombre? Ana
***
Ana
***

Conceptos practicados:
- input
- función len()
- formateo

Notas:
Para este ejercicio hemos utilizado la función len() que devuelve el
númeor de carácteres del objeto string.
"""

# Solución
nombre_user = input("\nCúal es tu nombre: ")
print(f"{"*" * len(nombre_user)}\n")
print(f"{nombre_user}\n")
print(f"{"*" * len(nombre_user)}\n")
