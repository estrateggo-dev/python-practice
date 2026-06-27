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

###
# CASTING A VALORES int()
###

# Convertir float -> int
print(int(3.9))
print(int(-3.39))
print(int(3.0))
print(int(3.5))

# Convertir de string -> int
print(int("42"))
print(int(" 42 "))
# print(int("42.0")) ERROR
# print(int("hola")) ERROR
# print(int("")) ERROR
# print(int(" ")) ERROR

# Convertir de bool -> int
print(int(True))
print(int(False))

###
# CASTING A VALORES float()
###

# Convertir int -> float
print(float(5))
print(float(-8))

# Convertir string -> float
print(float("30.5"))
print(float("-3.99"))
print(float("100"))
print(float(" 5.98  "))
# print(float("hola")) ERROR
# print(float("")) ERROR
# print(float(" ")) ERROR

# Convertor bool -> float
print(float(True))
print(float(False))

###
# CASTING A VALORES string()
###

# Cnvertir int -> string
print(str(42))
print(str(-16))

# Convertir float -> string
print(str("3.1416"))
print(str(-0.002))

# Convertir bool -> string
print(str(True))
print(str(False))

# Convertor None -> string
print(str(None))

###
# CASTING A VALORES bool()
###

# Convertir int -> bool
print(bool(5))
print(bool(0))
print(bool(-6))

# Convertir float -> bool
print(bool(3.1426))
print(bool(0.0))
print(bool(-7.6))

# Convertir string -> bool
print(bool("Hola"))
print(bool(""))
print(bool("  "))

# Convertor None -> bool
print(bool(None))
