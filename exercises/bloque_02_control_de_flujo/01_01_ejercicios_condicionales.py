import os

os.system("clear")

"""
Ejercicio 01 - nivel básico

Enunciado:
Escribe un programa que pida un número al usuario y diga si es positivo,
negativo o cero

Conceptos practicados:
- condicionaes
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
numero = int(input("Introduzca un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número introducido es el cero")

# Otra manera
print(
    f"{numero} {'es positivo' if numero > 0 else 'es negativo' if numero < 0 else 'es cero' }"  # noqa: E501
)

"""
Ejercicio 02 - nivel básico

Enunciado:
Escribe un programa que pida la edad del usuario y muestre si puede:

- Votar (>= 18)
- Conducir un turismo (>= 18)
- Jubilarse (>= 65)

Conceptos practicados:
- condicionales
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
edad = int(input("\nIntroduzca su edad: "))

if edad >= 18:
    print("\n✔️ Puede votar, es mayor de edad")
    print("✔️ Puede conducir un turismo, tiene la edad legal para ello")
else:
    print("\n❌ NO puede votar, es menor de edad")
    print("❌ NO puede conducir un turismo, es menor de edad")

if edad >= 65:
    print("✔️ Tiene edad suficiente para jubilarse\n")
else:
    print("❌ Debe esperar a cumplir los 65 años para poder jubilarse\n")


"""
Ejercicio 03 - nivel básico

Enunciado:
Pida dos números y muestre cuál es mayor, o si son iguales

Conceptos practicados:
- condicionales
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
num1 = int(input("Introduzca el número 1 (entero): "))
num2 = int(input("Introduzca el número 2 (entero): "))

if num1 == num2:
    print(f"\n{num1} son iguales {num2}\n")
elif num1 > num2:
    print(f"\n{num1} es mayor que {num2}\n")
else:
    print(f"\n{num2} es mayor que {num1}\n")


"""
Ejercicio 04 - nivel básico

Enunciado:
Escribe un clasificador de triángulos. Pide tres lados y determina si el
triángulo es:

- Equilatero (los tres lados iguales)
- Isósceles (exactamente dos lados iguales)
- Escaleno (níngúnb lado igual)

Recuerda también verificar que los tres lados puedan formar un triángulo (la suma de dos
lados cualesquiera debe ser mayor que el tercero).

Conceptos practicados:
- condicionales
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
lado_a = int(input("Introduzca el valor de lado 1 (entero): "))
lado_b = int(input("Introduzca el valor de lado 2 (entero): "))
lado_c = int(input("Introduzca el valor de lado 3 (entero): "))

if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
    print("Introduzca un valor positivo para los lados")
elif (
    lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a
):
    print("ERROR, no se cumple las condiciones para generar un triángulo")
elif lado_a == lado_b == lado_c:
    print("\nTres lados iguales, es un triángulo Equílatero\n")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("\nDos lados iguales, es un triángulo Isósceles\n")
else:
    print("\nNingún lado igual, es un triángulo Escaleno\n")


"""
Ejercicio 05 - nivel intermedio

Enunciado:
Crea un programa de acceso a un sistema, Define usuario y contraseña como constantes. El
programa debe pedir las credenciales y mostrar si el acceso fue concebido o denegado,
indicando si el error fue en el usuario, la contraseña o ambos

Conceptos practicados:
- condicionales
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

USUARIO = "administrador"
CONTRASEÑA = "Cleopatra525"

user = input("Introduzca nombre de Usuario: ")
password = input("Introduzca la contraseña: ")

print()

if USUARIO == user and CONTRASEÑA == password:
    print("✅ Acceso Concedido")
elif USUARIO != user and CONTRASEÑA != password:
    print("❌ ERROR, Usuario y Contraseña INCORRECTOS")
elif USUARIO != user:
    print("❌ ERROR, ha introducido un usuario INCORRECTO")
else:
    print("❌ ERROR, ha introducido una contraseña INCORRECTA")


"""
Ejercicio 06 - nivel intermedio

Enunciado:
Escribe una calculadora básica. Pide dos números y una operación (+, -, *, /). Realiza
la operación correspondiente y muestra el resultado, Maneja el caso de división por cero
y el de operación no reconocida

Conceptos practicados:
- condicionales
- match/case
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()
operando1 = int(input("Introduzca operando 1 (entero): "))
operacion = input("Introduzca la operación deseada (+, -, *, /): ").strip()
operando2 = int(input("Introduzca operando 2 (entero): "))

print(f"\nNúmero 1    : {operando1}")
print(f"Operación   : {operacion}")
print(f"Número 2    : {operando2}")

match operacion:
    case "+":
        print(f"Resultado: {operando1 + operando2}")
    case "-":
        print(f"Resultado   : {operando1 - operando2}")
    case "*":
        print(f"Resultado   : {operando1 * operando2}")
    case "/":
        if operando2 == 0:
            print("❌ ERROR: no se puede dividir por cero")
        else:
            print(f"Resultado   : {operando1 / operando2:.2f}")
    case _:
        print("❌ ERROR: operación no reconocida\n")


"""
Ejercicio 07 - nivel intermedio

Enunciado:
Crea un clasificador del índice de masa corporal (IMC). Pide peso en Kg y altura en
metros, calcula el IMC (peso / altura²) y clasifícalo:

• < 18.5 -> Peso Bajo
• 18.5 - 24.9 -> Peso Normal
• 25.0 - 29.9 -> Sobrepeso
• >= 30 -> Obesidad

Conceptos practicados:
- condicionales
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

peso = float(input("Introduzca el peso (Kg): "))
altura = float(input("Introduzca la altura (m): "))

imc = peso / altura**2

if imc >= 30:
    print(f"Su IMC es {imc:.1f} ->  🔴 Indica obesidad 🔴")
elif imc >= 25:
    print(f"Su IMC es {imc:.1f} ->  ⚠️ Indica sobrepeso ⚠️")
elif imc >= 18.5:
    print(f"Su IMC es {imc:.1f} ->  ✔️ Indica peso normal ✔️")
else:
    print(f"Su IMC es {imc:.1f} ->  🟡 Indica peso bajo 🟡")


"""
Ejercicio 08 - nivel intermedio

Enunciado:
Escribe un programa que diga si un año es bisiesto o no usando la condición
completa:

• Divisible por 4, Y
• No divisible por 100, O
• Divisible por 400

Usa el operador ternario para la línea final de salida

Conceptos practicados:
- operador ternario
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

anio = int(input("Introduzca el año: "))

print(
    f"\n{anio} : {'Es bisiesto' if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0 else '\nNo es bisiesto'}"  # noqa: E501
)

"""
Ejercicio 09 - nivel avanzado

Enunciado:
Crea un sistema de tarifas de transporte. El precio base es 2.50 €. Aplica descuentos
según estas reglas (pueden cumularse):

• Menores de 12 años: 50% de descuento
• Mayores de 65 años: 40% de descuento
• Tarjeta de socio: 10% adicional
• Horario nocturno (22:00 - 6:00): 20% de recargo

Pide la edad, si tiene tarjeta de socio (s/n) y la hora actual. Muestra el precio final
desglosado

Conceptos practicados:
- condicionales
- operadores
- expresiones

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

PRECIO_BASE = 2.5
DESCUENTO_MENOR = 0.5
DESCUENTO_SENIOR = 0.4
DESCUENTO_SOCIO = 0.1
RECARGO_NOCTURNO = 0.2

edad = int(input("Introduzca la edad: "))
tarjeta_socio = input("Tiene tarjeta de socio (s/n): ").lower().strip()
horas = int(input("Introduzca la Hora (formato 24H): "))
minutos = int(input("Introduza los Minutos: "))

descuento_infantil = 0
descuento_senior = 0
descuento_socio = 0
recargo_horario = 0


print()

print("=" * 7, "DESGLOSE TICKET", "=" * 7, "\n")
print(f"Hora Ticket  {horas}:{minutos}\n")

if edad < 12:
    descuento_infantil = PRECIO_BASE * DESCUENTO_MENOR
    print("✅ Descuento Infantil Aplicado")

elif edad >= 65:
    descuento_senior = PRECIO_BASE * DESCUENTO_SENIOR
    print("✅ Descuento Senior aplicado")

if tarjeta_socio == "s":
    descuento_socio = PRECIO_BASE * DESCUENTO_SOCIO
    print("✅ Descuento de socio aplicado")

if 22 <= horas <= 24 or 1 <= horas <= 6:
    recargo_horario = PRECIO_BASE * RECARGO_NOCTURNO
    print("✅ Recargo horario")

print()

total_descuentos = descuento_infantil + descuento_senior + descuento_socio
precio_final = PRECIO_BASE - total_descuentos + recargo_horario

print("=" * 30)
print(f"Precio Base         :   {PRECIO_BASE} €")
if descuento_infantil:
    print(f"Descuento Infantil  : - {descuento_infantil:.2f} €")
if descuento_senior:
    print(f"Descuento Senior  : - {descuento_senior:.2f} €")
if descuento_socio:
    print(f"Descuento Socio     : - {descuento_socio:.2f} €")
if recargo_horario:
    print(f"Recargo Horario     : + {recargo_horario:.2f} €")

print("-" * 30)
print(f"TOTAL A PAGAR       :   {precio_final} €\n")
