import os

os.system("clear")


"""
Ejercicio 01 - dificultad alta

Enunciado:

Pide al usuario:
• Edad
• Si tiene entrada, respondiendo "si" o "no"
• Si tiene invitación especial, respondiendo "si" o "no"

Reglas:
• Si la edad es menor que 0 , muestra "Edad no válida"
• Si la edad es menor que 16, muestra "Acceso Denegado: edad insuficiente"
• Si tiene entrada, muestra "Acceso permitido"
• Si no tiene entrada pero tiene invitación y tiene 18 años o más, muestra
  "Acceso permitido con invitación especial"
• En cualquier otro caso, muestra "Acceso denegado"

Conceptos practicados:
- validaciones múltiples
- operador 'and', 'or'
- prioridad de condiciones

Notas:
No usar listas ni funcinoes, primero valida la edad, cuida el orden: una
persona menor de 16 no puede entrar aunque tenga entrada.
"""

# Solución
edad_usuario = int(input("Introduzca su edad: "))
entrada_evento = input("Tiene entrada (si/no): ")
invitacion_evento = input("Tiene invitación al evento (si/no): ")

print()

if edad_usuario < 0:
    print(" ❌ Edad no válida")
elif edad_usuario < 16:
    print("❌ Acceso denegado: edad insuficiente")
elif entrada_evento == "si":
    print("✅ Acceso permitido")
elif entrada_evento == "no" and invitacion_evento == "si" and edad_usuario >= 18:
    print("✅ Acceso permitido con invitación especial")
else:
    print("❌ Acceso denegado")


"""
Ejercicio 02 - dificultad alta

Enunciado:

Pide al usuario el numero de horas que ha estado aparcado

Valida:
• Si las horas son menores o iguales que 0, muestra "Horas no válidas"

Si el dato es válido, calcula el precio:
• Hasta 1 hora: 2 €
• Mas de 1 y hasta 3 horas: 5 €
• Más de 3 y hasta 6 horas: 8 €
• Más de 6 y hasta 12 horas: 12 €
• Más de 12 horas: 20 €

Después aplica estas reglas adicionales:
• Si las horas superan 24, muestra "Estancia demasiado larga" y no
  calcules el precio
• Si las horas estan entre 0 y 24, muestra el precio final

Conceptos practicados:
- rangos
- validación
- calculos según tramos
- condiciones ordenadas

Notas:
Primero valida horas menores o iguales que 0, despues valida si
supera 24. Solo muestra el precio se las horas son válidas y no
superan 24
"""

# Solución
print()

horas_parking = float(input("Introduzca número de horas que ha estado aparcado: "))

print()

if horas_parking <= 0:
    print("❌ Horas no válidas")
elif horas_parking > 24:
    print("⚠️ Estancia demasiado larga ⚠️")
else:
    if horas_parking <= 1:
        coste_parking = 2
    elif horas_parking <= 3:
        coste_parking = 5
    elif horas_parking <= 6:
        coste_parking = 8
    elif horas_parking <= 12:
        coste_parking = 12
    else:
        coste_parking = 20
    print(f"Coste Parking: {coste_parking} €")

"""
Ejercicio 03 - dificultad alta

Enunciado:

Pide al usuario:
• Importe de la compra
• Si es cliente premiun, respondiendo "sí"o "no"
• Distancia de envío en Km

Valida primero:
• Si el importe es menor o igual que 0, muestra "Importe no válido"
• Si la distancia es menor que 0, muestra "Distancia no válida"

Si los datos son válidos, calcula el descuento:
• Si el importe es menor que 50, no hay descuento
• Si el importe está entre 50 y 99.99, descuento del 5%
• Si el importe está entre 100 y 199.99, descuento del 10%
• Si el importe es 200 o más, descuento del 15%

Después calcula el envio":
• Si la distancia es 0, envío gratis
• Si la distancia está entre 1 y 20, el envío cuesta 5 €
• Si la distancia está entre 21 y 100, el envio cuesta 10 €
• Si la distancia es mayor que 100, el envió cuesta 20 €

Regla premium:
• Si es cliente premium y el importe es mayor o igual que 100
  el envío es grstis.

Muestra:
• Importe inicial
• Descuento aplicado
• Coste de envío
• Total final

Conceptos practicados:
- validaciones
- rangos
- cálculo
- condiciones múltiple

Notas:
• No uses listas
• No uses funciones
• No uses diccionarios
• Calcula primero el descuento, luego el envío y finalmente el total
• Solo muestra el resumen si todos los datos son válidos
"""

# Solución
print()

importe_compra = float(input("Introduzca el importe de la compra (€): "))
cliente_premium = input("¿Es usted cliente premium (sí/no): ")
distancia_envio = float(input("Introduzca la distancia de envío (Km): "))

print()

if importe_compra <= 0:
    print("❌ Importe no válido")
elif distancia_envio < 0:
    print("❌ Distancia no válida")
else:
    if importe_compra < 50:
        descuento_compra = 0
    elif importe_compra < 100:
        descuento_compra = importe_compra * 0.05
    elif importe_compra < 200:
        descuento_compra = importe_compra * 0.1
    else:
        descuento_compra = importe_compra * 0.15

    if distancia_envio == 0:
        coste_envio = 0
    elif distancia_envio <= 20:
        coste_envio = 5
    elif distancia_envio <= 100:
        coste_envio = 10
    else:
        coste_envio = 20

    if cliente_premium == "sí" and importe_compra >= 100:
        coste_envio = 0

    total_compra = importe_compra - descuento_compra + coste_envio

    print()
    print("=" * 7, "TICKET COMPRA", "=" * 7)
    print(f"Importe compra     : {importe_compra:.2f} €")
    print(f"Descuento aplicado : - {descuento_compra:.2f} €")
    print(f"Coste envío        : + {coste_envio:.2f} €")
    print(f"Total final        : {total_compra:.2f} €")
