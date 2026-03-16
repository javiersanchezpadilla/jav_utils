""" Este programa muestra el uso de los f-string con su 
    mini-lenguaje de especificación deformato
    
    Vamos a diseñar un Ticket de Venta profesional. Este ejercicio 
    es perfecto porque nos obliga a usar alineación (para que los 
    nombres no se muevan), separadores de miles (para que se vea contable)
    y formatos de fecha.

    ^40         Centramos el título del ticket para que quede justo a la mitad
                de nuestra línea de 40 guiones.
    <25 y >15   Creamos columnas invisibles. El nombre del producto tiene 25 
                espacios a la izquierda y el precio 15 a la derecha. Esto evita 
                que los precios se muevan si un nombre es más largo que otro.
    14,.2f:     
        14      Reserva el espacio.
        ,       Pone la coma de miles (25,400.50).
        .2f     Asegura que siempre veamos dos decimales, aunque sea .00.

    %H:%M       Usamos las directivas de tiempo para que la hora se vea limpia.
"""
from datetime import datetime

# Datos de la compra
cliente = "Juan Pérez"
fecha = datetime.now()
producto1 = "Laptop Gamer"
precio1 = 25400.50
producto2 = "Mouse"
precio2 = 550.00
impuesto_porcentaje = 0.16

subtotal = precio1 + precio2
iva = subtotal * impuesto_porcentaje
total = subtotal + iva

# Construcción del Ticket usando f-strings
print("-" * 40)
print(f"{'MI TIENDITA TECH':^40}") # Centrado en 40 espacios
print("-" * 40)

# Formato de Fecha: día/mes/año hora:minuto
print(f"Fecha: {fecha:%d/%m/%Y %H:%M}")
print(f"Cliente: {cliente}")
print("-" * 40)

# Encabezados de tabla (Alineación)
# <25 significa: a la izquierda en 25 espacios
# >15 significa: a la derecha en 15 espacios
print(f"{'Producto':<25}{'Precio':>15}")

# Cuerpo del ticket (Moneda con miles y 2 decimales)
print(f"{producto1:<25}${precio1:>14,.2f}")
print(f"{producto2:<25}${precio2:>14,.2f}")
print("-" * 40)

# Resumen financiero
print(f"{'Subtotal:':<25}${subtotal:>14,.2f}")
print(f"{'IVA (16%):':<25}${iva:>14,.2f}")
print(f"{'TOTAL:':<25}${total:>14,.2f}")
print("-" * 40)
print(f"{'¡GRACIAS POR SU COMPRA!':^40}")