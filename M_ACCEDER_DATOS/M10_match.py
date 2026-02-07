""" El encargado de laboratorio le pide a un asistente que haga un programa que
    al escribir el nombre de una sustenaica, el sistema debe mostrar si es 
    sólido, liquido o gaseoso, para evitar errores básicos de maniúlación"""

sustancia = input("Ingrese la sustancia: ")

match sustancia:
    case "hierro":
        print("Es solido")
    case "mercurio":
        print("es liquido")
    case "dioxido de carbono":
        print("es gaseoso")
    case _:
        print("Sustancia no reconocida")
