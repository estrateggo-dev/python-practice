###
# 02 - types()
# Python tinene varios tipos de datos, veamos cuales son
# int, float, complex, str, bool, NoneType, list, tuple, range, dict, set
###

# Tipo int() : números enteros, positivos o negativos, sin decimales
# La funbción type() nos permite conocer el tipo de dato de una variable
# Python permite número realmente grandes, solo dependeremos de la memoria disponible
print("int:")
print(type(10))
print(type(0))
print(type(-15))
print(type(3545654564654654654))

print(546523123135416546454665465)
print(546523123135416546454665465 + 1)
print("\n")

# Tipo float(): número de coma flotante, positivos o negativos, con decimales
# La notación científica tambien se considera un float
print("float:")
print(type(3.14))
print(type(0.25))
print(type(-0.75))
print(type(12.021244445447447))
print(type(1e5))
print(12.021244445447447)
print(12.021244445447447 + 1.05)
print(3e3)
print("\n")

# Tipo complex(): número complejos, con parte real y parte imaginaria
print("complex:")
print(type(1 + 2j))

# Tipo str(): cadenas de texto
print("str:")
print(type("Esto es una cadena"))
print(type(""))
print(type("123"))
print(type("""
    Multilinea
"""))
print("\n")

# Tipo bool(): tipo que representa los valores "True" o "False"
# Las comparaciones de números también devuelve valores booleanos
# Todas las operaciones de lógica devuelven un booleano
print("bool:")
print(type(True))
print(type(False))
print(type(1 > 2))
print(False)
print(True)
print(5 > 3)
print(0 < 3)

# Tipo NoneType(): es el tipo de dato representado por el valor <None>
# Representa la ausencia de valor, valor no definido, valor vacio intencionado
# Se puede utilizar para indicar que una variable aún no tiene valor
# Para comprobar si una función ha encontrado algo
print(type(None))
print(None)
