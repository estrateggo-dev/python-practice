###
# 05 - inpyt()
# Esta función nos permite introducir información, nos permite comunicarnos
# con el usuario a través de la consola. Tenemos que tener en cuenta que
# todo lo recogamos por consola será un sting
###

nombre = input("Hola, ¿Cómo te llamas?: ")

edad = int(input("Qué edad tienes: "))
print(f"Te llamas {nombre} y naciste en {2026 - edad}\n")

# También podemos obtener múltiples valores a la vez, es decir, podemos
# al usuario varios valores a la vez pero deberemos utilizar la
# función split() - las rspuestas tiene que estar separada por espacio
pais, ciudad = input("¿En que pais y ciudad vives?: ").split()
print(f"Estás viviendo en {pais},en {ciudad}")
