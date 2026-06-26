###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado automátivo y de tipad fuerte
###

# Para asignar una variable solo tenemos qu hacer lo siguiente:
my_name = "Rodrigo"

print(my_name)

# Las variables se pueden reasignar en tiempo de ejecución
edad = 29
print(edad)

edad = 31
print(edad)

# Tipado Dinámico: el tipo de dato se determina en tiempo de ejecución
# no hay que declararlo explicitamente
name = "Alejandro"
print(type(name))

name = 32
print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipo automáticamente, por ejemplo
# no dejaría hacer algo como print(10 + "2"), nos diría que no podemos juntar un
# número con un strinf, para poder hacer esto tenemos los f-strings:
edad = 19
nombre = "Jose"

print(f"Mi nombre es {nombre} y tengo {edad} años")

# Mala praxis para asignar variables
nombre, edad, ciudad = "Pedro", 29, "Barcelona"

# Convenciones de nombres de variables: snake_case
nombre_usuario = "Sandro"
edad_usuario = 25
precio_oferta_producto = 15

# En Python no existe las constantes, pero existe una convención para
# su utilización: UPPER_CASE -> constantes
NUMERO_PI = 3.1416
MI_CONSTANTE = 0.10

# No podemos tener como nombres de variables que sean palabras reservadas
# por Python, podemos consultar la lista para conocerlas

# Podemos tipar de manera directa una variable, pero tenemos que tener en
# cuenta que Python esto solo lo tomará como una anotación si en tiempo
# de ejcución cambiamos el tipo lo ejecutará sin problema, el editor si
# nos avisará (Activar Type Checking Mode: strict)
is_user_logged_in: bool = True
print(is_user_logged_in)

# is_user_logged_in = 42
print(is_user_logged_in)
