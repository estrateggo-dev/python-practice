"""
Ejercicio 01 - nivel básico

Enunciado:
Sin ejecutar el código, calcula el resultado de cada expresión y explica el
orden de evaluación:

- print(2 + 3 * 4 - 1)
- print(10 / 2 + 8 // 3)
- print(2 ** 3 ** 2)
- print(15 % 4 + 2 ** 2)
- print((2 + 3) * (4 - 1))

Conceptos practicados:
- expresiones
- operadores
- orden evaluación

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución

# Expresión 1: print(2 + 3 * 4 - 1)
#   Evaluación: 3*4=12 ; 2 + 12 - 1 = 13

# Expresión 2: print(10 / 2 + 8 //3)
#   Evaluación: 10/2=5 ; 8//3=2 ; 5 + 2 = 7

# Expresión 3: print(2 ** 3 ** 2)
#   Evaluación: 3**2=9 ; 2 ** 9 = 512

# Expresión 4: print(15 % 4 + 2 ** 2)
#   Evaluación: 2**2=4 ; 15%4= ; 4 + 3 = 7

# Expresión 5: print((2 + 3) * (4 - 1))
#   Evaluación: 2+3=5 ; 4-1=3 ; 5 * 3 = 15

"""
Ejercicio 02 - nivel básico

Enunciado:
Escribe expresiones en Python para calcular cada uno de estos resultados. Usa
variables con nombres descriptivos:

- El área de un rectangulo de 7.5 metros de ancho y 4.2 metros de alto
- El perímetro de un cículo de radio 5 (usa 3.14159 para PI)
- El porcentaje que representa 37 sobre 200
- La hipotenusa de un triángulo rectángulo con catetos 3 y 4 (usa ** 0.5
  para la raíz)

Conceptos practicados:
- expresiones
- operadores

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución


base = 7.5
altura = 4.2
area = base * altura

print(f"El area del rectángulo de {base} de base y {altura} de altura es: {area} m²\n")

PI = 3.14159
radio = 5
perimetro = 2 * PI * radio

print(f"El Perímetro de un círculo de {radio} de radio es: {perimetro:.2f}\n")

parte = 37
total = 200
porcentaje = parte / total * 100

print(f"El porcentaje de {parte} sobre {total} = {porcentaje:.2f} %\n")

cateto1 = 3
cateto2 = 4
hipotenusa = (3**2 + 4**2) ** 0.5

print(
    f"La hipotenusa de un triángulo de catetos {cateto1} & {cateto2} "
    f"es: {hipotenusa:.2f}\n"
)

"""
Ejercicio 03 - nivel básico

Enunciado:
Escribe las condiciones en Python (quedevuelvan True o False) para comprobar:

- Si un numero n es par
- Si un número n es divisible por 3 y 5 a la vez
- Si una edad está en el rango de 18 a 65 (ambos inclusive)
- Si un texto contiene la palabra "Python"
- Si una variable valor no es None

Conceptos practicados:
- expresiones
- operadore


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
numero = 5
print(numero % 2 == 0)

numero = 15
print(numero % 3 == 0 and numero % 5 == 0)

texto = "Python mola mucho"
print("Python" in texto)

valor = None
print(valor is not None, "\n")

"""
Ejercicio 04 - nivel intermedio

Enunciado:
Crea un programna que pida dos números y muestre el resultado de todas las
operaciones aritméticas entre ellos, incluyendo el manejo del caso que el
divisor sea cero

Conceptos practicados:
- operadores aritméticos
- expresiones
- manejo excepciones

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
num1 = int(input("Introduzca el número 1: "))
num2 = int(input("Introduzca el número 2: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
potencia = num1**num2

print(f"\nPrimer número  :   {num1}")
print(f"Segundo Número : {num2}")
print("-" * 30)
print(f"Suma                 : {suma}")
print(f"Resta                : {resta}")
print(f"Multiplicación       : {multiplicacion}")

if num2 != 0:
    print(f"División             : {num1 / num2:.1f}")
    print(f"División Entera      : {num1 // num2}")
    print(f"Módulo (resto)       : {num1 % num2}")
else:
    print("División             : ❌ No se puede dividir por cero")
    print("División Entera      : ❌ No se puede dividir por cero")
    print("Módulo (resto)       : ❌ No se puede dividir por cero")

print(f"Potencia             : {potencia}\n")

"""
Ejercicio 05 - nivel intermedio

Enunciado:
Escribe un programa que pida la edad de una persona y determine, usando
operadores lógicos si:

- Es menor de edad (<18)
- Es mayor de edad y joven (18-35)
- Es de mediana edad (36-60)
- Es mayor de 60

Muestra el grupo al que pertenece

Conceptos practicados:
- expresiones
- operadores lógicos

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
edad = int(input("Introduzca la edad (>= 0): "))
grupo = None

if edad < 18:
    grupo = "Es menor de edad"
elif 18 <= edad <= 35:
    grupo = "Es mayor de edad y joven"
elif 36 <= edad <= 60:
    grupo = "Es de mediana edad"
else:
    grupo = "Es mayor de 60"

print("\n", grupo, "\n")

"""
Ejercicio 06 - nivel intermedio

Enunciado:
Predice la salida de cada una de las líneas antes de ejecutar. Luego comprueba:

- print(5 > 3 and 2 < 4)
- print(5 > 3 or 2 > 4)
- print(not 5 > 3)
- print(5 > 3 and not 2 > 4)
- print("a" in "hola")
- print("z" not in "hola")
- print(bool(0 or "" or [] or "Python"))
- print(bool(1 and 2 and 3))
- print(0 or "hola" or "mundo")
- print(None or 0 or "" or 42)

Conceptos practicados:
- operadores
- expresiones

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución

# Expresión1: print(5 > 3 and 2 < 4)
#   Salida -> True

# Expresión 2: print(5 > 3 or 2 > 4)
#   Salida -> True

# Expresión 3: print(not 5 > 3)
#   Salida -> False

# Expresión 4: print(5 > 3 and not 2 > 4)
#   Salida -> True

# Expresión 5: print("a" in "hola")
#   Salida -> True

# Expresión 6: print("z" not in "hola")
#   Salida -> True

# Expresión 7: print(bool(0 or "" or [] or "Python"))
#   Salida -> True

# Expresión 8: print(bool(1 and 2 and 3))
#   Salida -> True

# Expresión 9: print(0 or "hola" or "mundo")
#   Salida -> "hola"

# Expresión 10: print(None or 0 or "" or 42)
#   Salida -> 42


"""
Ejercicio 07 - nivel intermedio

Enunciado:
Escribe un validador de contraseñas. La contraseña introducida por el usuario debe
cumplir todas estas condiciones:

- Longitud mínima de 8 caracteres
- Contiene al menos un dígit
- No contiene espacios

Conceptos practicados:
- expresiones
- operadores
- validación campos

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
contraseña = input("Introduzca la contraseña: ")

validar_longitud = len(contraseña) >= 8
validar_digitos = any(c.isdigit() for c in contraseña)
validar_espacios = " " not in contraseña

if validar_longitud and validar_digitos and validar_espacios:
    print(
        "\n✔️ Longitud correcta (8+ caracteres)"
        "\n✔️ Contiene al menos un dígito"
        "\n✔️ Sin espacios"
    )
    print("\n✅ La contraseña es válida\n")
else:
    print("\n❌ La contraseña no es válida\n")

    if not validar_longitud:
        print("❌ La contraseña tiene menos de 8 caracteres\n")

    if not validar_digitos:
        print("❌ La contraseña no contiene ningún dígito\n")

    if not validar_espacios:
        print("❌ La contraseña contiene espacios vacíos\n")


"""
Ejercicio 08 - nivel avanzado

Enunciado:
Sin ejecutar el código, predice el resultado en cada expresión y justifica paso a paso
las reglas de predecencia:

- print(2 + 3 > 4 and 10 - 2 * 3 == 4)
- print(not False and not 0 and not "")
- print(True + True * False - True)
- print("" or 0 or None or [] or "encontrado")
- print(5 and 0 or 3)
- print(4 or 0 and 3)

Conceptos practicados:
- operadores
- expresiones
- precedencia

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución

# Expresión 1: print(2 + 3 > 4 and 10 - 2 * 3 == 4)
#   Salida -> True
#           (10 - 2 * 3) -> 10 - 6 = 4
#           4 == 4 True
#           (2 + 3 > 4) -> 5 > 4 True
#           True and True -> True

# Expresión 2: print(not False and not 0 and not "")
#   Salida -> True
#           not False and not 0 -> true and True -> True
#           True and not "" -> True and True -> True

# Expresión 3: print(True + True * False - True)
#   Salida -> 0
#           1 + 1 * 0 - 1 -> 1 + 0 - 1 -> 0

# Expresión 4: print("" or 0 or None or [] or "encontrado")
#   Salida -> "encontrado"
#           False or False or None or False or True
#           Devuelve primer valor True -> "encontrado"

# Expresión 5: print(5 and 0 or 3)
#   Salida -> 3
#           True and False or True
#           False or True -> True
#           Devuelve el primer valor True -> 3

# Expresión 6: print(4 or 0 and 3)
#   Salida -> 4
#           0 and 3 : False and True -> False
#           4 or False : True or False -> True
#           Devuelve primer valor True -> 4

"""
Ejercicio 09 - nivel avanzado

Enunciado:
Escribe una calculadora de IMC (Índice de Masa Corporal). El programa debe pedir
peso (Kg) y altura (m), calcular el IMC y clasificarlo:

- IMC < 18.5: Bajo peso
- 18.5 ≤ IMC < 25: Peso normal
- 25 ≤ IMC < 30: Sobrepeso
- IMC ≥ 30: Obesidad

Conceptos practicados:
- operadores
- expresiones

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
peso = float(input("Introduzca el peso (Kg): "))
altura = float(input("Introduzca la altura (m): "))

IMC = peso / (altura**2)

print(f"\nPeso (Kg)    : {peso}")
print(f"Altura (m)   : {altura}\n")
print(f"IMC          : {IMC:.2f}")

if IMC < 18.5:
    print("Categoría    : Bajo Peso\n")
elif 18.5 <= IMC < 25:
    print("Categoría    : Peso normal\n")
elif 25 <= IMC < 30:
    print("Categoría    : Sobrepeso\n")
else:
    print("Categoría    : Obesidad\n")


"""
Ejercicio 10 - nivel avanzado

Enunciado:
Crea un programa que dado un año, determine si es bisiesto usando una sola expresión
booleana. Un año es bisiesto si:

- Es divisible por 4, and
- No es divisible por 100, or
- Si es divisible por 400

Conceptos practicados:
- expresiones
- operadores


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
es_bisiesto = False
año = int(input("Introduzca un año: "))


if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    es_bisiesto = True

print(f"{año} es bisiesto: {es_bisiesto}\n")
