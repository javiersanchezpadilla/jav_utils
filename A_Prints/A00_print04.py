""" Ajustes de estilo

    end El finalizador.

    Por defecto: Al final de cada print(), se presiona la tecla "Enter" 
    automáticamente.
    Con end: Tú le dices a Python: "No pases de página todavía, mejor pon 
    esto al final".

    Parámetro,¿Qué hace?,Valor por defecto
    ------------------------------------------
    sep     Lo que se pone entre cada dato.                 Un espacio "" 
    end     Lo que se pone al final de todo el mensaje.     "salto de línea ""\n

    
"""
# Lo normal (salta de línea automáticamente)
print("Hola")
print("Mundo")
# Salida:
# Hola
# Mundo

# Cambiando el final por un espacio para que no salte
print("Hola", end=" ")
print("Mundo")
# Salida: Hola Mundo (¡Todo en una sola línea!)

# Haciendo una barra de carga simple
print("Cargando", end="...")
print(" [EXITO]")
# Salida: Cargando... [EXITO]

# Colocando todo junto
print("Vagón 1", "Vagón 2", "Vagón 3", sep=" == ", end=" [FIN DEL TREN]")
