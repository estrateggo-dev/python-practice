###
# 03 - casting de types
# El casting transforma un tipo de valor a otro
# La transformación entre tipos tiene que se compatible para que pueda darse
###

print("Conversion de tipos:")
print(type(int("100")))
print("\n")

# De cadena a entero
print(int("100") + 2)
# De entero a cadena
print("100" + str(2))
print("\n")

# De cadena a float
print(float("3.1416"))
# De float a cadena
print(str(3.14616) + "999")
print("\n")

# De float entero (pierde precisión - elimina los decimales)
print(int(3.1242587))
print(int(3.8954465456))
print("\n")

# De entero a booleano
print(bool(3))
print(bool(0))
# De booleano a entero
print(int(True))
print(int(False))
print("\n")


# De float a booleano
print(bool(-3.5))
print(bool(0.0))
# De booleano a float
print(float(True))
print(float(False))
print("\n")

# De cadena a booleano
print(bool(""))
print(bool(" "))
print(bool("False"))
# De booleano a cadena
print(str(False))
print(str(True))
print(type(str(False)))
print(type(str(True)))
