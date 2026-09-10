edad = 50

if edad < 18:
    print("Es muy joven")
elif edad >= 18 and edad <= 20:
    print("Sigue siendo muy joven")
elif edad > 20 and edad < 30:
    print("Es un poco mayor")
elif edad >= 30 and edad <= 40:
    print("Se puede considerar")
else:
    print("Bienvenido")
    
# El resultado anterior se puede obtener de la siguiente forma
estatus = { (edad < 18): "Es muy joven",
            (18 <= edad <= 20): "Sigue siendo muy joven",
            (20 < edad < 30): "Es un poco mayor",
            (30 <= edad <= 40): "Se puede considerar",
            (edad > 40): "Bienvenido"
}[True]

print(estatus)
    