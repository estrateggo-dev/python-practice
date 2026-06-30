import os

os.system("clear")

"""
Ejercicio 01 - dificultad media

Enunciado:
Pide una nota entre 0 y 10, luego muestra:

• Suspenso: si la nota es menor que 5
• Aprobado:  si está entre 5 y 6.99
• Notable: si está entre 7 y 8.99
• Sobresaliente: si está entre 9 y

Conceptos practicados:
- Condicinoales
- Expresiones
- Operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nota_alumno = float(input("Introduzca la nota recibida (0-10): "))

print()

if nota_alumno >= 9:
    print(f"Nota: {nota_alumno} -> Calificación: Sobresaliente")
elif nota_alumno >= 7:
    print(f"Nota: {nota_alumno} -> Calificación: Notable")
elif nota_alumno >= 5:
    print(f"Nota: {nota_alumno} -> Calificación: Aprobado")
else:
    print(f"Nota: {nota_alumno} -> Calificación: Suspenso")


"""
Ejercicio 02 - dificultad media

Enunciado:
Pide al usuario una temperatura en grados Celsius, luego muestra:

• "El agua está congelada" si la temperatura es menor o igual a 0
• "El agua esá líquida"si está entre 1 y 99
• "El agua está hirviendo" si es 100 o más

Conceptos practicados:
- condicionales
- operadores
- expresiones

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

celsius = float(input("Introduzca la temperatura (°C): "))

print()

if celsius >= 100:
    print(f"Temperatura °{celsius} -> El agua está hirviendo")
elif celsius >= 1:
    print(f"Temperatura: °{celsius} -> El agua está líquida")
else:
    print(f"Temperatura: °{celsius} -> El agua está congelada")


"""
Ejercicio 03 - dificultad media

Enunciado:
Pide al usuario el precio de un producto, si el precio de mayor o igual
que 100, aplica un descuento del 10%. Si no, no aplica descuento. Mostrar
el precio final.

Conceptos practicados:
- condicionales
- operaciones aritméticas
- comparacion

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

precio_producto = float(input("Introduzca el precio del producto: "))

if precio_producto >= 100:
    precio_final = precio_producto * 0.9  # aplica 10% de descuento
else:
    precio_final = precio_producto

print(f"El precio final es: {precio_final} €\n")


"""
Ejercicio 04 - dificultad alta

Enunciado:
Pide al usuario un nombre de usuario y una contraseña, el acceso
solo se concederá sí:

• Usuario: "admin"
• Contraseña: "1234"

Conceptos practicados:
- comparacion de cadenas
- condicionales
- operador 'and'

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

nombre_usuario = input("Introduzca nombre de usuario: ").strip()
password = input("Introduzca una contraseña: ")

print()

if nombre_usuario == "admin" and password == "1234":
    print("✅ Acceso concedido")
else:
    print("❌ Acceso Denegado")


"""
Ejercicio 05 - dificultad alta

Enunciado:
Pide al usuario su edad y clasificala así:

• Menor de 0: "Edad no válida"
• 0 a 12: "Niño"
• 13 a 17: "Adolescente"
• 18 a 64: "Adulto"
• 65 o más: "Persona mayor"

Conceptos practicados:
- condicionales
- rangos


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

edad_usuario = int(input("Introduzca su edad (> 0): "))

print()

if edad_usuario >= 65:
    print(f"Edad: {edad_usuario} -> Persona Mayor")
elif edad_usuario >= 18:
    print(f"Edad: {edad_usuario} -> Adulto")
elif edad_usuario >= 13:
    print(f"Edad: {edad_usuario} -> Adolescente")
elif edad_usuario >= 0:
    print(f"Edad: {edad_usuario} -> Nino")
else:
    print("Edad no válida")


"""
Ejercicio 06 - dificualta alta

Enunciado:
Pide al usuario su salario mensual, calcula el impuesto con estas
reglas:

• Si el salario es menor que 1000, no paga impuestos
• Si el salario está entre 1000 y 2999,99, paga un 10%
• Si el salario es 3000 o más, paga un 20%

Muestra:
• El salario introducido
• El impuesto calculado
• El salario final después de restar el impuesto

Conceptos practicados:
- condicionales
- operaciones aritméticas
- porcentajes

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

salario_usuario = float(input("Introduzca el salario: "))

print()

if salario_usuario >= 3000:
    impuesto = salario_usuario * 0.2
elif salario_usuario >= 1000:
    impuesto = salario_usuario * 0.1
else:
    impuesto = 0

salario_final = salario_usuario - impuesto

print(f"Salario: {salario_usuario} €")
print(f"Impuestos: {impuesto} €")
print(f"Salario final: {salario_final} €")
