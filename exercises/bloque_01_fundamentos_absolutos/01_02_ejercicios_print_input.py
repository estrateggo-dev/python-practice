"""
Ejercicio 01 - nivel avanzado

Enunciado:
Vamos a eleborar un recibo simple, donde se pida al cliente:
- Nombre del cliente
- Producto comprado
- Precio del producto
- Fecha de compra

Conceptos practicados:
- input()
- f-strings
- organización de salida

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
nombre_cliente = input("Introduzca su nombre: ")
producto_cliente = input("Introduzca el Producto comprado: ")
precio_producto = float(input("Introduzca el precio del producto: "))
fecha_compra = input("Introduzca la fecha de compra: ")

print(f"{"=" * 12} RECIBO {"=" * 12}\n")
print(f"\tCliente: {nombre_cliente}")
print(f"\tProducto: {producto_cliente}")
print(f"\tPrecio: {precio_producto} €")
print(f"\tFecha: {fecha_compra}\n")
print(f"{'GRACIAS POR SU COMPRA':^32}")
print(f"{"=" * 32}\n")
