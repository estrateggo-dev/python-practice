import os

os.system("clear")

"""
Ejercicio 01 - Dificualta baja

Enunciado:
Pida una nota entre 0 y 10. Muestra:

• "Nota no válida" si la nota es menor que 0 o mayor que 10
• "Suspenso" si esta entre 0 y 4.99
• "Aprobado" si está entre 5 y 6.99
• "Notable"si está entre 7 y 8.99
• "Sobresaliente" si está entre 9 y 10


Conceptos practicados:
- rangos
- condicionales


Notas:
Primero debes mostrar si la nota es válida o no
"""

# Solución
nota_usuario = float(input("Introduzca la nota: "))

print()

if nota_usuario < 0 or nota_usuario > 10:
    print("❌ Nota no válida")
elif 9 <= nota_usuario >= 9:
    print(f"Nota: {nota_usuario} -> Sobresaliente")
elif nota_usuario >= 7:
    print(f"Nota: {nota_usuario} -> Notable")
elif nota_usuario >= 5:
    print(f"Nota: {nota_usuario} -> Aprobado")
else:
    print(f"Nota: {nota_usuario} -> Suspenso")


"""
Ejercicio 02 - dificultad baja

Enunciado:
Pide al usuario la velocidad de un vehículo en Km/h, luego muestra:

• "Valocidad no válida" si es menor que 0
• "Vehículo detenido"si es 0
• "Velocidad baja" si está entre 1 y 50
• "Velocidad normal" si está entre 51 y 120
• "Exceso de velocidad" si es mayor que 120

Conceptos practicados:
- rangos numéricos
- condiciones ordenadas


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

velocidad_usuario = int(input("Introduzca la velocidad: "))

if velocidad_usuario > 120:
    print(f"Velocidad: {velocidad_usuario} -> 🔴 Exceso de velocidad 🔴")
elif velocidad_usuario > 50:
    print(f"Velocidad: {velocidad_usuario} -> 🟢 Velocidad normal 🟢")
elif velocidad_usuario > 0:
    print(f"Velocidad: {velocidad_usuario} -> 🟡 Velocidad baja 🟡")
elif velocidad_usuario == 0:
    print(f"Velocidad: {velocidad_usuario} -> 🚗 Vehículo detenido 🚗")
else:
    print("❌ Velocidad no válida")


"""
Ejercicio 03 - dificultad baja

Enunciado:
Pide al usuario su edad, luego muestra:

• "Edad no válida" si es menor que 0
• "Entrada grauita" si tiene entre 0 y 5 años
• "Entrada infantil" si tiene entre 6 y 12 años
• "Entrada juvenil" si tinene entre 13 y 17
• "Entrada adulta" si tiene 18 o más

Conceptos practicados:
- rangos
- validación simple


Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

edad_usuario = int(input("Introduzca la edad: "))

print()

if edad_usuario >= 18:
    print(f"Edad: {edad_usuario} -> Entrada adulta")
elif edad_usuario >= 13:
    print(f"Edad: {edad_usuario} -> Entrada juvenil")
elif edad_usuario >= 6:
    print(f"Edad: {edad_usuario} -> Entrada infantil")
elif edad_usuario >= 0:
    print(f"Edad: {edad_usuario} -> Entrada gratuita")
else:
    print("❌ Edad no válida")


"""
Ejercicio 04 - dificultad media

Enunciado:
Pide al usuario el porcentaje de batería de un dispositivo, luego muestra:

• "Porcentaje no válido" si es mejor que 0 o mayor que 100
• "Batería crítica" si está entre 0 y 10
• "Batería baja" si está entre 11 y 30
• "Batería media" si está entre 31 y 70
• "Batería alta" si está entre 71 y 100

Conceptos practicados:
- rangos
- validación
- porcentajes

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

bateria_usuario = int(input("Introduzca el nivel de batería: "))

print()

if bateria_usuario < 0 or bateria_usuario > 100:
    print("❌ Porcentaje no válido")
elif bateria_usuario > 70:
    print(f"Nivel batería: {bateria_usuario} -> Batería alta")
elif bateria_usuario > 30:
    print(f"Nivel batería: {bateria_usuario} -> Batería media")
elif bateria_usuario > 10:
    print(f"Nivel batería: {bateria_usuario} -> Batería baja")
else:
    print(f"Nivel batería: {bateria_usuario} -> Batería crítica")


"""
Ejercicio 05 - dificultada media

Enunciado:
Pida una temperatura en rgados Celsius, luego muestre:

• "Frio extremo" si es menor que -10
• "Frío" si está entre -10 y 9.99
• "Templado" si está ente 10 y 24.99
• "Calor" si está ente 25 y 34.99
• "Calor extremo" si es 35 o más

Conceptos practicados:
- rangos con números negativos
- orden de condiciones


Notas:
usa 'float'
"""

# Solución
print()

temperatura = float(input("Introduzca la temperatura: "))

print()

if temperatura < -10:
    print(f"Temperatura: {temperatura} -> 🥶 Frio extremo 🥶")
elif temperatura < 10:
    print(f"Temperatura: {temperatura} -> 🔵 Frio 🔵")
elif temperatura < 25:
    print(f"Temperatura: {temperatura} -> 🟢 Templado 🟢")
elif temperatura < 35:
    print(f"Temperatura: {temperatura} -> 🔴 Calor 🔴")
else:
    print(f"Temperatura: {temperatura} -> 🔥 Calor extremo 🔥")


"""
Ejercicio 06 - dificultad media

Enunciado:
Pide al usuario cuantos KWh ha consumido en un mes, luego muestra:

• "Consumo no válido" si el consumo es menor que 0
• "Consumo bajho" si está entre 0 y 100
• "Consumo medio" si está entre 100.01 y 300
• "Consumo alto" si está entre 300.01 y 600
• "Consumo excesivo" si es mayor que 600

Despues si el consumo es va'lido, calcula el coste así:

• Hasta 100 KWh: es 0.12 € por KWh
• Más de 100 y  hasta 300: 0.18 € por KWh
• Más de 300: 0.25 € por KWh

Conceptos practicados:
- rangos
- calculo
- condicionales

Notas:
No es una tarifa progresiva por tramos. Se aplica un único precio por KWh según
el consumo total
"""

# Solución
print()

consumo_luz = float(input("Introduzca el consumo de luz este mes (KWh): "))
consumo_valido = True

print()

if consumo_luz > 600:
    print(f"Consumo Luz: {consumo_luz} KWh -> Consumo excesivo")
    coste = consumo_luz * 0.25
elif consumo_luz > 300:
    print(f"Consumo Luz: {consumo_luz} KWh -> Consumo alto")
    coste = consumo_luz * 0.25
elif consumo_luz > 100:
    print(f"Consumo Luz: {consumo_luz} KWh -> Consumo medio")
    coste = consumo_luz * 0.18
elif consumo_luz >= 0:
    print(f"Consumo Luz: {consumo_luz} KWh -> Consumo bajo")
    coste = consumo_luz * 0.12
else:
    print("❌ Consumo no válido")
    consumo_valido = False

if consumo_valido:
    print(f"El importe de la factura asciende a : {coste:.2f} €")


"""
Ejercicio 07 - dificultad media

Enunciado:
Pide al usuario su peso en Kg y su altura en metros, luego muestra:

• "Datos no válidos" si el peso o la altura son menores o iguales que 0
• "Bajo peso" si el IMC es menor que 18.5
• "Sobrepeso" si está entre 25 y 29.99
• "Obesidad" si es 30 o más

Conceptos practicados:
- operaciones aritméticas
- rangos
- validación

Notas:
No se puede usar funciones propias y no redondeees si no quieres. Puedes
mostrar el IMC tal como salga
"""

# Solución
print()

peso_usuario = float(input("Introduzca su peso (Kg): "))
altura_usuario = float(input("Introduzca su altura (m): "))

if peso_usuario <= 0 or altura_usuario <= 0:
    print("❌ Datos no válidos")
else:
    imc = peso_usuario / (altura_usuario * altura_usuario)

    if imc >= 30:
        print(f"IMC: {imc:.2f} -> Obesidad")
    elif imc >= 25:
        print(f"IMC: {imc:.2f} -> Sobrepeso")
    elif imc >= 18.5:
        print(f"IMC: {imc:.2f} -> Peso normal")
    else:
        print(f"IMC: {imc:.2f} -> Bajo peso")


"""
Ejercicio 08 - dificultad alta

Enunciado:

Pide al usuario:
• Limite de velocidad de la vía
• Velocidad real del vehículo

Primero valida:
• Si el límite es menor o igual que 0, muestra "Límite no válido"
• Si la velocidad real es menor que 0, muestra "Velocidad no válida"

Si los datos son válidos, calcula el exceso, luego muestra:
• "Sin multa" si el exceso es menor o igual que 0
• "Multa leve" si el exceso está entre 1 y 20
• "Multa grave" si el exceso está entre 21 y 40
• "Multa muy grave" si el exceso es mayor que 40

Además, muestra el exceso de velocidad solo si hay multa

Conceptos practicados:
- rangos
- cálculo
- condiciones encadenadas

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
print()

limite_velocidad = int(input("Introduzca el límite de velocidad de la vía: (Km/h): "))
velocidad_real = int(input("Introduzca la velocidad real del vehículo: "))

exceso = velocidad_real - limite_velocidad

print()

if limite_velocidad <= 0:
    print("❌ Límite no válido")
elif velocidad_real < 0:
    print("❌ Velocidad no válida")
elif exceso <= 0:
    print("✅ Velocidad correcta")
elif exceso <= 20:
    print(f"Exceso: {exceso} Km/h -> Multa leve")
elif exceso <= 40:
    print(f"Exceso: {exceso} Km/h -> Multa grave")
else:
    print(f"Exceso: {exceso} Km/h -> Multa muy grave")


"""
Ejercicio 09 - dificultad alta

Enunciado:

Pide al usuario:
• Peso del paquete en Kg
• Distancia del envío en Km

Valida primero:
• Si el peso es menor o igual que 0, muestra "Peso no válido"
• Si la distancia es menor o igual que 0, muestra "Distancia no válida"

Si los datos son válidos, calcula el precio base según el peso:

• Hasta 1 Kg: 5 €
• Más de 1 Kg y hasta 5 Kg: 10 €
• Más de 5 Kg y hasta 10 Kg: 20 €
• Más de 10 Kg: 30 €

Después aplica suplemento por distancia:
• Hasta 100 Km: sin suplemento
• Más de 100 Km y hasta 500 Km: suma 5 €
• Más de 500 Km: suma 10 €

Muestra el reocio final del envío

Conceptos practicados:
- rangos
- validacion
- condiciones múltiples

Notas:
No uses lsitas ni diccionarios, usa variables como precio_base, suplemento y
precio_final
"""

# Solución
print()

peso_paquete = float(input("Introduzca el peso (Kg): "))
distancia_envio = float(input("Introduzca la distancia (Km): "))

if peso_paquete <= 0:
    print("❌ Peso no válido")
elif distancia_envio <= 0:
    print("❌ Distancia no válida")
else:
    if peso_paquete <= 1:
        precio_base = 5
    elif peso_paquete <= 5:
        precio_base = 10
    elif peso_paquete <= 10:
        precio_base = 20
    else:
        precio_base = 30

    if distancia_envio <= 100:
        suplemento = 0
    elif distancia_envio <= 500:
        suplemento = 5
    else:
        suplemento = 10

    precio_final = precio_base + suplemento

    print("====== RESUMEN ENVÍO ======")
    print(f"Precio base : {precio_base} €")
    print(f"Suplemento  : {suplemento} €")
    print(f"Precio final: {precio_final} €")


"""
Ejercicio 10 - dificultad alta

Enunciado:

Pide al usuario:
• Edad
• Salario mensual
• Cantidad socicitada para el préstamo

Valida primero:
• Si la edad es menor que 18, muestra "Prestamo rechazado: edad insuficiente"
• Si el salario es menor o igual que 0, muestra"Pretamos rechazado: salario no válido"
• Si la cantidad socicitada es menor o igual que 0, muestra: "Prestamo rechazado:
  cantidadno válida"

Si los datos son válidos, evalua:
• Si el salario es menor que 1200, muestra "Prestamo rechazado: salario insuficiente"
• Si la cantidad solicitada es mayor que (salario * 10) muestra "Prestamos rechazado:
  cantidad demasiado alta"
• Si la edad solicitada está entre 18 y  25 y la cantidad solicitada es mayor que
  (salario * 5), muestra "Restamos rechazado: riesgo alto"
• En cualquier otro caso, muestra "Prestamo aprobado"

Conceptos practicados:
- rangos
- validacion
- operador 'and'
- calculo de porcentajes

Notas:
El orden de las condiciones importa, no usar funciones, listas ni diccionarios
"""

# Solución
print()

edad_cliente = int(input("Introduzca su edad: "))
salario_cliente = float(input("Introduzca su salario mensual (€): "))
monto_prestamo = float(input("Introduzca la cantidad prestamos solicitada (€): "))
prestamo_valido = True

print()

if edad_cliente < 18:
    print("❌ Prestamo rechazado: edad insuficiente")
    prestamo_valido = False
elif salario_cliente <= 0:
    print("❌ Prestamo rechazado: salario no válido")
    prestamo_valido = False
elif monto_prestamo <= 0:
    print("❌ Prestamo rechazado: cantidad no válida")
    prestamo_valido = False

if prestamo_valido:
    if salario_cliente < 1200:
        print(
            f"Salario: {salario_cliente} -> ❌ Prestamo rechazado: salario insuficiente"
        )
    elif monto_prestamo > salario_cliente * 10:
        print(
            f"Monto solicitado: {monto_prestamo} -> ❌ Prestamo rechazado: cantidad demasiado alta"  # noqa: E501
        )
    elif 18 <= edad_cliente <= 25 and monto_prestamo > salario_cliente * 5:
        print("❌ Prestamo rechazado: riesgo alto")
    else:
        print("✅ Prestamo aprobado")
