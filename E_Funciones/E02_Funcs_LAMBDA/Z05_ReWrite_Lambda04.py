""" SOBRE ESCRIBIR FUNCIONES CON FUNCIONES LAMBDA

    Sobre escritura de un método en una instancia (no la clase)
    -----------------------------------------------------------
    En este ejemplo se sobre escribira un método de la instancia una vez
    creada la clase, mediante la función LAMBDA.
    Al moficiar el método de la instancia, no modifica el comportamiento
    del método de la clase, lo hace de forma particular solamente para la 
    instancia u objeto.
"""

class Perro:
    def sonido_que_emite(self):
        return 'Ladrar'
    

# Creamos la instancia (el objeto)
mi_perro = Perro()

# Modificamos el método pero SOLO PARA LA INSTANCIA!!!
mi_perro.sonido_que_emite = lambda: 'Maulla'

# Verificamos el método moficado
print('Método de la instancia:', mi_perro.sonido_que_emite())

# Verificamos que no haya cambiado el Método de la clase (ya que no se toco)
print('Método de la CLASE:', Perro().sonido_que_emite())
