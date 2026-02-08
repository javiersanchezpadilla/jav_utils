""" Esto lo debemos eviar a toda costa, ya que puede generar problemas
    de seguridad y errores en el código.
    Ya que nos puede generar problemas de seguridad ya que se puede
    ejecutar código malicioso (inyección de código).
    En su lugar, se recomienda usar eval() con precaución y solo con
    datos de confianza.
    En este ejemplo, se muestra cómo usar eval() para evaluar una expresión
    matemática simple, pero se debe evitar su uso en aplicaciones reales.
    Si en lgar quere evaluar algo como 5+6-2, se puede hacer de la siguiente manera:
    eval('print("Hola")') donde el resultado es Hola"""


while True:
    operacion = input("Ingrese una operación matemática (o 'salir' para terminar): ")
    if operacion.lower() == 'salir':
        print("Saliendo del programa.")
        break
    try:
        resultado = eval(operacion)
        print(f"El resultado de '{operacion}' es: {resultado}")
    except Exception as e:
        print(f"Error al evaluar la operación: {e}")
        print("Asegúrese de ingresar una operación válida.")

# Nota: Este código es un ejemplo educativo y no se recomienda su uso en producción.
# Evite el uso de eval() con entradas no confiables para prevenir inyecciones de código.
# En aplicaciones reales, considere usar alternativas más seguras como
# funciones matemáticas específicas o bibliotecas de evaluación de expresiones.
