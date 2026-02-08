""" SOBRE ESCRIBIR FUNCIONES CON FUNCIONES LAMBDA

    Sobre escritura de solo una INSTANCIA
    -------------------------------------
    En este ejemplo se sobre escribira una función de un método 
    Se sobre escribira la función sleep(), reemplazando su comportamiento
    aquí solo desplegará el texto sin hacer el retardo del tiempo.
"""

class MiClase:
    def mi_metodo(self):
        return "METODO DEFINIDO EN LA CLASE"
    

# Definimos una instancia
prueba = MiClase()

# Sobre esribimos el método unicamente de esa instancia
prueba.mi_metodo = lambda: "Metodo MODIFICADO Desde la INSTANCIA"

# Verificamos el método en la instnacia
print('El método de mi instancia u objeto da:', prueba.mi_metodo())

# Veerificamos si se modificó el método original de la clase
print('El método desde la clase', MiClase().mi_metodo())
