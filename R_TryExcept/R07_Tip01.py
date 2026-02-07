""" ERRORES CON Try... Except

    Estamos acostumbrados a poner todo dentro del try (como espaguetti)

        try:
            s = '10'
            numero = int(s)
            resultado = numero + perdido
            print(resultado)

        except Exception:
            print('Algo salio mal')

    La forma correcta de hacer bien las cosas es:
    ---------------------------------------------
    try:
        print('Realiza las cosas peligrosas')
    except ValueError:
        print('Manipula el error')
    else:
        print('Ejecuta el código solo cuando este todo correcto')
    finally:
        print('Siempre se ejecutara')

    EJEMPLO
    -------
    try:
        numero = int(input())
    except ValueError:
        print('No es un número')
    else:
        print('Es un número valido')
    finally:
        print('Listooooo!!!!!')

    Última recomendación: nunca escribas
        except Exception:
"""

try:
    numero = int("10")
    explota = numero / 0
except ValueError:
    print('No es un número')
except ZeroDivisionError:
    print('Este es el problema real')

