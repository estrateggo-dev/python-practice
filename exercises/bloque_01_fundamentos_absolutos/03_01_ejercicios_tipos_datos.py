"""
Ejercicio 01 - nivel básico

Enunciado:
Sin ejecutar código, escribe que tipo devolvera type() para cada variable y
luego compruebalo:

a = 100
b = 100.0
c = "100"
d = True
e = None
f = 10 / 2
g = 10 // 2

Conceptos practicados:
- tipos datos
- type()
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución


import math

print(type(100))  # a -> int
print(type(100.0))  # b -> float
print(type("100"))  # c -> string
print(type(True))  # d -> bool
print(type(None))  # e -> NoneType
print(type(10 / 2))  # f -> float
print(type(10 // 2), "\n")  # g -> int

"""
Ejercicio 02 - nivel básico

Enunciado:
Convierte los siguientes valores y muestra el resultdo junto a su tipo:

int("357)"
float("3.14")
str(2024)
bool(0)
bool("Python")
int(True)
float(False)

Conceptos practicados:
- casting
- tipos datos
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print(int("357"))
print(type(int("357")), "\n")

print(float("3.14"))
print(type(float("3.14")), "\n")

print(str(2024))
print(type(str(2024)), "\n")

print(bool(0))
print(type(bool(0)), "\n")

print(bool("Python"))
print(type(bool("Python")), "\n")

print(int(True))
print(type(int(True)), "\n")

print(float(False))
print(type(float(False)), "\n")

"""
Ejercicio 03 - nivel básico

Enunciado:
Pide al usuario su nombre, edad y altura (en metros). Asegurate de convertir
cada tipo al valor correcto. Muestra un resultado formateado

Conceptos practicados:
- casting
- tipos datos
- input(), print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre_user = input("Introduzca su nombre: ")
edad_user = int(input("Introduzca su edad: "))
altura_user = float(input("Introduza su altura (en metros): "))

print(
    f"\nNombre : {nombre_user}\nEdad   : {edad_user} años\nAltura : {altura_user} m\n"
)

"""
Ejercicio 04 - nivel intermedio

Enunciado:
Escribe un programa que pida un número decimal al usuario y que muestre:

- Su valor redondeado al entero más cercano (round())
- Su valor truncado al entero inferior (int())
- Si es positivo, negativo o cero (bool())
- Su representación como string

Conceptos practicados:
- casting
- tipos datos
- round()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
numero_decimal = float(input("Introduzca un número decimal: "))

print(f"\nValor redondeado : {round(numero_decimal)}\n")

print(f"Valor Trundado: {int(numero_decimal)}\n")

if numero_decimal > 0:
    print("El número introducido es positivo\n")
elif numero_decimal < 0:
    print("El numero decimal es negativo\n")
else:
    print("El numero decimal es cero\n")


"""
Ejercicio 05 - nivel intermedio

Enunciado:
Demuestra el problema de la precisión de los floats. Muestra tres ejemplos
distintos de operaciones con decimales que no dan el resultado exacto
esperado. Luego corrige cada uno de ellos usando round () o math.isclose()

Conceptos practicados:
- tipos datos
- roud()
- math.isclose()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
resultado_1 = 0.1 + 0.2
esperado = 0.3

print("=" * 40, "\n")
print("EJEMPLO 1 : 0.1 + 0.2")
print("\n", "=" * 40, "\n")

print(f"Resultado obtenido: {resultado_1}")
print(f"Resultado esperado: {esperado}")
print(f"¿Son iguales con ==?: {resultado_1 == esperado}\n")

print(f"Corrección con round(): {round(resultado_1, 2) == esperado}")
print(f"La suma de ambos números con round() es: {round(resultado_1, 2)}\n")

print(f"Corrección con math.isclose(): {math.isclose(resultado_1, esperado)}\n")

"""
Ejercicio 06 - nivel intermedio

Enunciado:
Escribe un programa que pida precio y cantidad, calcule el subtotal, el IVA (125)
y el total. Muestra todos los valores exactamente 2 decimales usado f-strings

Conceptos practicados:
- f-strings
- tipos datos
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
precio = round(float(input("Introduzca el precio unitario: ")), 2)
cantidad = int(input("Introduzca la cantidad: "))
subtotal = precio * cantidad
cantidad_iva = subtotal * 0.21

print(f"\nPrecio Unitario: {precio}")
print(f"Cantidad: {cantidad}")
print("-" * 30)
print(f"Subtotal : {subtotal:.2f} €")
print(f"IVA (21%): {cantidad_iva:.2f} €")
print(f"Total    : {subtotal + cantidad_iva:.2f} €\n")

"""
Ejercicio 07 - nivel intermedio

Enunciado:
Investiga que devuelven estas operaciones y explica por qué:

- print(True + True + True)
- print(True * 100)
- print(False - 1)
- print(bool("0"))
- print(bool(0.0001))
- print(int("0xFF", 16))

Conceptos practicados:
- tipos datos
- print()


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución

# Expresión 1: print(True + True + True)
#   Devuelve 3 (los booleanos son subtipos de los enteros, en operaciones
#   con booleanos python trata a True = 1, False = 0)

# Expresion 2: print(True * 100)
#   Devuelve 100, como en el ejemplo anterior True tiene un valor de 1

# Expresión 3: print(False - 1)
#   Devuelve -1, False tiene un valor de 0

# Expresión 4: print(bool("0"))
#   Devuelve True, porque al hacer casting de un string no vacio da ese valor

# Expresión 5: print(bool(0.0001))
#   Devuelve True, al hacer casting a un float que no es 0.0 devuelve ese valor

# Expresión 6: print(int("0xFF", 16)) -> 0xFF número hexadecial (base 16) valor 255
#   Devuelve 255

"""
Ejercicio 08 - nivel avanzado

Enunciado:
Crea un convertidor de temperatura completo que pida la temperatura y la unidad de
origen (C, F o K) y la convierta a las otras dos. Usa constantes en UPER_CASE para
los factores de conversión y maneja los decimales con precición (2 cifras):

°F = °C * 9/5 + 32
K = °C + 273.15
°C = (°F - 32) * 5/9

Conceptos practicados:
- Concepto 1
- Concepto 2
- Concepto 3

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
temperatura = float(input("Introduzca la temperatura: "))
unidad_temperatura = input("Introduzca la unidad de temperatura (C/F/K): ")

print("\n" + "=" * 20 + " RESUMEN " + "=" * 20 + "\n")

print(f"Temperatura: {temperatura}")
print(f"Unidad (C/F/K): {unidad_temperatura}")
print("-" * 30)

if unidad_temperatura == "C":
    FARENHEIT = temperatura * 9 / 5 + 32
    KELVIN = temperatura + 273.15
    print(f"\n{temperatura:.2f} °C = {FARENHEIT:.2f} °F = {KELVIN:.2f} K\n")
elif unidad_temperatura == "F":
    CELSIUS = (temperatura - 32) * 5 / 9
    KELVIN = CELSIUS + 273.15
    print(f"\n{temperatura:.2f} °F = {CELSIUS:.2f} °C = {KELVIN:.2f} K\n")
else:
    CELSIUS = temperatura - 273.15
    FARENHEIT = CELSIUS * 9 / 5 + 32
    print(f"\n{temperatura:.2f} K = {CELSIUS:.2f} °C = {FARENHEIT:.2f} °F\n")


"""
Ejercicio 09 - nivel avanzado

Enunciado:
Sin ejecutar el código, predice el resultado de cada línea y explica por qué. Luego
comprueba tus respuestas:

- print(type(True + 0))
- print(type(1 + 1.0))
- print(type(int(3.9) + 0.0))
- print(bool("") == bool(0))
- print(None == False)
- print(None is False)
- print(int(bool("False")))
- print(str(None))

Conceptos practicados:
- tipos datos
- casting
- print()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución

# Expresión 1: print(type(True + 0))
#   Salida -> type: int

# Expresión 2: print(type(1 + 1.0))
#   Salida -> type: float

# Expresión 3: print(type(int(3.9) + 0.0))
#   Salida -> type: float

# Expresión 4: print(bool("") == bool(0))
#   Salida -> True

# Expresión 5: print(None == False)
#   Salida -> False

# Expresión 6: print(None is False)
#   Salida -> False

# Expresión 7: print(int(bool("False")))
#   Salida -> 1

# Expresión 8: print(str(None))
#   Salida -> None

"""
Ejercicio 10 - nivel avanzado

Enunciado:
Escribe un validador de datos para un formulario de registro. El programa debe
pedir: nombre(srt no vacio), edad (int entre 0 y 120), altura (float entre 0.5 y 2.5)
y activo (bool, el usuario escribe "si" o "no"). Para cada campo, verifica que el tipo
y el valor son correctos y muestra si la validación ha pasado o no.

Conceptos practicados:
- tipos datos
- if/else
- print(), input()

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre_usuario = input("Introduzca el nombre (string no vacio): ")
edad_usuario = int(input("Introduzca la edad (entre 0 - 120): "))
altura_usuario = float(input("Introduzca la altura (entre 0.5 - 2.5): "))
activo_usuario = input("¿Usuario activo? (si - no): ")

print("\n***  Registro de usuario  ***")
print(f"Nombre: {nombre_usuario}")
print(f"Edad: {edad_usuario}")
print(f"Altura: {altura_usuario:.2f}")
print(f"¿Activo? (si/no): {activo_usuario}\n")

print("\n***  Resultado de Validación  ***")

if nombre_usuario == "":
    print("Nombre     : ❌ Valor no válido\t(Debe ser un str no vacio)")
else:
    print(f"Nombre     : ✅ '{nombre_usuario}'\t(str no vacío)")


if 0 <= edad_usuario <= 120:
    print(f"Edad       : ✅ {edad_usuario}\t(int entre 0 y 120)")
else:
    print("Edad       : ❌ Valor no válido\t(Debe ser int entre 0 y 120)")


if 0.5 <= altura_usuario <= 2.5:
    print(f"Altura     : ✅ {altura_usuario:.2f}\t(float entre 0.5 y 2.5)")
else:
    print("Altura     : ❌ Valor no válido\t(Debe ser float entre 0.5 y 2.5)")

if activo_usuario == "si":
    print(f"Activo     : ✅ {True}\t(bool)\n")
else:
    print("Activo     : ❌ Valor no válido\t(Debe ser un valor booleano)\n")
