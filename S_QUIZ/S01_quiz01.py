""" 
    Para entenderlo, primero debemos separar dos conceptos: "Ser iguales" vs. 
    "Ser el mismo objeto".

    1. El concepto: == vs is
    == (Igualdad)       Pregunta: "¿Tienen el mismo contenido?". (Si dos gemelos 
                        tienen la misma ropa, son "iguales").
    is (Identidad)      Pregunta: "¿Son exactamente el mismo objeto en la 
                        memoria?". (¿Es la misma persona?).

    def modifica(lst=[1, 2]):  <-- lst=[1, 2] crea una lista "secreta" en la 
                                   memoria para el valor por defecto.
        lst = lst + [3]        <-- Al usar el signo +, Python crea una lista 
                                    totalmente nueva en una parte diferente de la 
                                    memoria. No modifica la lista original, sino 
                                    que hace una copia con el 3 añadido.
        return lst

    a = modifica()             <-- Toma [1, 2], le suma [3], crea una lista nueva 
                                   [1, 2, 3] y la guarda en la variable a.
    b = modifica()             <-- Vuelve a tomar el valor por defecto [1, 2], 
                                   le suma [3], crea otra lista nueva [1, 2, 3] 
                                   y la guarda en b. 

    print(a == b, a is b)      <-- a == b (True): Ambas listas contienen [1, 2, 3]
                                   Sus valores son idénticos, por eso da Verdadero.   
                                   a is b (False): Aunque se ven iguales, son dos 
                                   objetos distintos en la memoria (como dos casas 
                                   construidas con el mismo plano pero en terrenos 
                                   diferentes). Por eso da Falso.                   

¿Qué pasaría si cambiáramos una sola línea?
-------------------------------------------
Si en lugar de lst = lst + [3] usaras lst.append(3), el resultado sería muy diferente
con .append(), modificas la lista original directamente en lugar de crear una nueva. 
Debido a un comportamiento curioso de Python con los "argumentos por defecto mutables", 
la segunda vez que llamaras a la función, la lista ya tendría el 3 de la primera llamada.

"""

def modifica(lst=[1, 2]):
    lst = lst + [3]
    return lst

a = modifica()
b = modifica()

                        # Resultado True (a == b) ambas listas son identicas
                        # a is b (False): Aunque se ven iguales, son dos 
                        # objetos distintos en la memoria
print(a == b, a is b)   
