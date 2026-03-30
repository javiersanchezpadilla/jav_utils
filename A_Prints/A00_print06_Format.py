""" INYECCION DE VALORES EN UN STRING MEDIANTE EL USO DE FORMAT
"""

print("En la pelicula {} actua {}".format('La india maria', 'maria'))

# podemos especificar el orden como si fueran indices
print("El actor {1} actua en la pelicula {0}".format('La india maria', 'maria'))

hobbie = "A {} le encanta jugar {}"
print(hobbie.format('Francisco', 'Beisbol'))
print(hobbie.format('Angela', 'Basketball'))


# puede ubicar la inyección mediante una posición como si fuera un índice
pelicula = 'El actor {1} es excelente en la pelicula {0}'
print(pelicula.format('Forest Gump', 'Tom Hanks'))


# Podemos referenciar mediante nombres de variables
jugador = 'El jugador {nombre_jugador} juega en el equipo {nombre_equipo}'
print(jugador.format(nombre_equipo='Real Madrid', nombre_jugador='Ronaldiño'))
print(jugador.format(nombre_equipo='Barcelona', nombre_jugador='Messi'))


# Forma 4 de inyección F-String
nombre = 'Pedro Navajas'
curso = 'Python'
nivel = 'Avanzado'

texto = f'El profesor {nombre} enseña el curso {curso} nivel {nivel}'
print(texto)