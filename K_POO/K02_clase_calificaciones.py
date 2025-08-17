""" Ejemplo de una clase para realizar operaciones"""

class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def total_calificaciones(self):
        """ Calcula el total de las calificaciones """
        return sum(self.calificaciones)

    def promedio_calificaciones(self):
        """ Calcula el promedio de las calificaciones """
        if len(self.calificaciones) == 0:
            return 0
        return self.total_calificaciones() / len(self.calificaciones)

    def mostrar_informacion(self):
        """ Muestra la información del estudiante """
        print(f"Nombre: {self.nombre}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Total: {self.total_calificaciones()}")
        print(f"Promedio: {self.promedio_calificaciones():.2f}")


# Ejemplo de uso de la clase Estudiante
estudiante1 = Estudiante("Juan", [85, 90, 78, 92])
estudiante1.mostrar_informacion()

estudiante2 = Estudiante("Ana", [88, 76, 95])
estudiante2.mostrar_informacion()
# Salida esperada: