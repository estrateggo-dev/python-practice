###
# 01 - print()
# El módulo print() es el módulo que nos permite imprimmir en consola
# Sirve para mostrar informacin por consola
###

print("Hola mundo, desde España, desde la galaxia")
print("Este cometario tiene 'comillas simples' dentro de comillas dobles")

print("Python", "es", "genial")

# Por defecto, print() separa los argumentos con un espacio, pero podemos cambiarlo con
# el parámetro sep
print("Python", "es", "brutal", sep=" - ")

# Por defecto, print() termina con un salto de línea, pero podemos cambiarlo con el
# parámetro end
print("Esto se imprimme", end=" ")
print("en la misma línea")

# Hemos imprimdo cadenas de texto, pero también podemos imprimir números
print(1, 2, 3, 4, 5, sep=" - ")
print("\n")

# Función f-strings: permite incrustar expresiones dentro de una cadena de texto
nombre = "Ana"
apellido = "Lopez"
edad = 25

print(f"Me llamo {nombre}, mi apellido es {apellido}  y tengo {edad} años" + "\n")

precio = 10.99
unidades = 5

print(f"El total es : {precio * unidades} €" + "\n")

###
# 01 - input()
# El módulo input () sirve para pedir por consola un valor
# El valor de lo capturado es siempre un string
###

nombre1 = input("Introduzca su nombre: ")
print(f"El nombre del usuario es: {nombre1}" + "\n")

edad = int(input("Introduzca su edad: "))
print(f"La edad del usuario es {edad + 10 }" + "\n")

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

print(f"\nLa suma es: {num1 + num2}")
print(f"\nLa resta es: {num1 - num2}" + "\n")

###
# Carácteres de escape
###

print("Linea 1\nLinea 2\nLinea 3\n")
