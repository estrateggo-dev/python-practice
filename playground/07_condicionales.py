###
# 07 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones
###

import os

os.system("clear")

print("\nSentencia simple condicional")

edad = 18

if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad <= 71:
    print("Eres mayor de edad y estas en edad de trabajar")
else:
    print("Eres mayor de edad y además puedes jubilarte")

# Siempre que hacemos un tipo de comparación nos va a devolver un booleano

print("\nCondiciones múltiples (operadores lógicos - AND)")

edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("❌ No puede coger el coche")


print("\nCondiciones múltiples (operadores lógicos - OR)")

saldo = 10000
tienes_credito = True

if saldo >= 50000 or tienes_credito:
    print("Puedo comprarme la moto 🛵")
else:
    print("Tengo que ahorra más")

print("\nAnidar condicionales")

# Cuando podamos debemos evitar las anidaciones profundas

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la discoteca")


# Operador Ternario
# [código si se cumple la condición] if [condición] else [código si no cumple]

print("\nLa condición ternaria")

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

numero = int(input("Introduzca un númer: "))

tipo = "par" if numero % 2 == 0 else "impar"
print(f"{numero} es {tipo}")

puntuacion = 850
liga = (
    "oro" if puntuacion >= 1000 else
    "plata" if puntuacion >= 500 else
    "bronce"
)
print(f"Liga: {liga}")
