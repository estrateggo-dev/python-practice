"""
Ejercicio 01 - nivel básico

Enunciado:
Crea variables para almacenar la siguiente información sobre una persona
y luego imprimeas en una sola línea con print():
- nombre
- apellido
- edad
- ciudad

Conceptos practicados:
- variables
- print()
- input()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su apellido: ")
edad = int(input("Introduzca su edad: "))
ciudad = input("Introduzca la ciudad donde vive: ")

print(f"\n{nombre} {apellido} | {edad} años | {ciudad}\n")

"""
Ejercicio 02 - nivel básico

Enunciado:
Define una variable precio con el valor 100. Aplica un descuento del 15%
usando el operador *= y luego añade el IVA del 21% co otro *=. Imprime el
precio original, el precio con descuento y el precio final

Conceptos practicados:
- variables
- operadores asginación


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
precio = 100
print(f"El precio originales es: {precio} €")
precio *= 0.85
print(f"El precio con un descuento del 15% es: {precio} €")
precio *= 1.21
print(f"El precio final con un 21% IVA es: {precio} €\n")

"""
Ejercicio 03 - nivel básico

Enunciado:
Usa la asignación paralela para definir en una sola línea: x = 5,
y = 10, z = 15. Luego imprime su suma

Conceptos practicados:
- variables
- asignacion
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
x, y, z = 5, 10, 15
print(f"La suma de los tres números es: {x + y + z}\n")

"""
Ejercicio 04 - nivel básico

Enunciado:

Razonar que va a imprimir el siguiente código:
a = 5
b = a
a = 10

print(a)
print(b)

Conceptos practicados:
- variables
- asignación
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
# print(a) -> 5
# print(b) -> 5
# Ambas variables apuntan al mismo contenedor
a = 5
b = a
print(f"{a}")
print(f"{b}\n")

"""
Ejercicio 05 - nivel intermedio

Enunciado:
Crea un prograna que pida al usuario su nombre y año de nacimiento, calcule
su edad aproximada y muestre un mensaje. Usa nombres de variables descriptivos

Conceptos practicados:
- variables
- input()


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre_usuario = input("¿Cúal es su nombre?: ")
año_nacimiento = int(input("¿Cúal es su año de nacimiento?: "))

print(f"¡Hola {nombre_usuario}!, tienes aproximadamente {2026 - año_nacimiento} años\n")

"""
Ejercicio 06 - nivel intermedio

Enunciado:
Implementa el intercambio de dos variables sin usar una variable temporal.
El programa debe pedir dos números al usuario, intercambiarlos y mostrar el
resultado

Conceptos practicados:
- variables
- asignación
- input()
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))

print(f"\nEl valor de numero 1 es: {numero1}, el valor de numero 2 es: {numero2}\n")

numero1, numero2 = numero2, numero1

print(
    f"Ahora el valor de numero 1 es: {numero1} y el valor de numero 2 es: {numero2}\n"
)

"""
Ejercicio 07 - nivel intermedio

Enunciado:
Crea un programa de "caja registradora" simple. Define una variable total = 0.0 y súmale
tres precios distintos usando +=. Muestra el total al final

Conceptos practicados:
- variables
- asignación
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
total = 0.0
precio1 = 5.5
precio2 = 8
precio3 = 3.25

total += precio1
total += precio2
total += precio3

print(f"El importe total acumulado es de: {total}\n")

"""
Ejercicio 08 - nivel avanzado

Enunciado:
Analiza este código e identifica todos los errores (hay al menos 5). No
lo ejcutes: razónalos leyendo el código

1er_nombre = "Ana"
apellido-materno = "Lopez"
print = "error aquí"
edad actual = 25
if = True
total = precio * 3

Conceptos practicados:
- variables


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
# Error 1: una variable no puede empezar por un número
# Error 2: una variable no puede separarse por un guión
# Error 3: no se puede utilizar la palabra reservada print como nombre de variable
# Error 4: no puede haber espacios entre el nombre de una variable
# Error 5: if es una palabra reservada, no se puede utilizar como nombre de variable
# Error 6: la variable precio no se ha inicializado antes de utilizarla

"""
Ejercicio 09 - nivel avanzado

Enunciado:
Escribe un prograna que convierta una temperatura de Celsius a Frenheit y a Kelvin.
Usa nombre de variables descriptivos y constante en UPER_CASE para los factores
de conversion, las formulas son:

- F = C * 9/5 + 32
- K = C + 273.15

Conceptos practicados:
- variables


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
celsius = float(input("Introduzca la temperatura en grasdos Celsius: "))

farenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"\nTemperatura en Celsius: {celsius}\n{celsius}° = {farenheit}°F = {kelvin}K\n")

"""
Ejercicio 10 - nivel avanzado

Enunciado:
Sin ejecutar el código, predice el valor que imprimirá cada print(). Luego ejecutelos
para comprobar:

x = 10
y = x
x += 5
print(x)  ¿?
print(y)  ¿?

-----------
a, b = b, a = 1, 2
print(a)  ¿?
print(b)  ¿?

----------
n = 2
n = n * n
n = n * n
print(n)  ¿?

Conceptos practicados:
- variables
- print()


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
###### A #######
# print(x) -> 15
# print(y) -> 10

###### B ######
# print(a) -> 2
# print(b) -> 1

###### C ######
# print(n) -> 16

x = 10
y = x
x += 5
print(f"{x}")
print(f"{y}\n")

a, b = b, a = 1, 2
print(f"{a}")
print(f"{b}\n")

n = 2
n = n * n
n = n * n
print(f"{n}\n")
