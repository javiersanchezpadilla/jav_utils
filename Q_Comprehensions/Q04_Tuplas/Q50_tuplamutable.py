""" ¿cuando declaramos una tupla con elementos mutables como listas, estas 
    pueden cambiarse,me refiero a los valores de la lista contenida de la 
    tupla, se que las tuplas son no mutables, sin embargo me surge la duda 
    de si es posible?

    Sí, puedes cambiar los valores de la lista que está dentro de la tupla.
    =======================================================================

    Parece una contradicción, ¿verdad? Vamos a entenderlo con una analogía muy 
    sencilla.

    La Analogía: El maletín encadenado
    ----------------------------------
    Imagina que una Tupla es un maletín de seguridad que está encadenado a la 
    mesa.
    La inmutabilidad de la tupla significa que no puedes cambiar el maletín 
    por otro, ni puedes quitarlo de la mesa, ni puedes añadir más maletines a 
    la cadena.
    Sin embargo, si dentro del maletín guardaste una Lista (que es como una 
    libreta de notas), ¡nada te impide abrir el maletín y escribir o borrar 
    cosas en esa libreta!

    La "cadena" (la tupla) sigue intacta, sujetando el mismo objeto. Lo que 
    cambió fue el contenido interno de ese objeto.
    
    ¿Por qué sucede esto? (Explicación técnica simple)
    --------------------------------------------------
    En Python, la tupla no guarda los datos directamente, sino que guarda las 
    direcciones de memoria (referencias) de los objetos.

    La tupla dice: "En mi posición 1 siempre estará el objeto que vive en la 
    dirección 0x123".
    Como la lista es mutable, ella puede cambiar sus valores internos sin 
    necesidad de mudarse de dirección de memoria.
    Para la tupla, nada ha cambiado: ella sigue apuntando al mismo objeto en 0x123.

    ¿Cuándo es útil esto?
    ---------------------
    Se usa poco, porque la idea de una tupla es que sea constante. Pero puede ser 
    útil si tienes una estructura fija (como los datos de un usuario) pero quieres 
    que uno de esos campos sea una lista que crezca con el tiempo (como su historial 
    de compras).

    Un pequeño consejo: Si quieres que nada, absolutamente nada cambie, asegúrate 
    de que todo lo que metas en la tupla sean también elementos inmutables (números, 
    textos u otras tuplas).
"""
# Creamos una tupla que contiene una lista
# Posición 0: Un número (inmutable)
# Posición 1: Una lista (mutable)
mi_tupla = (10, ["rojo", "azul"])

print("Original:", mi_tupla)

# Intentar cambiar el 10 daría error: mi_tupla[0] = 20 (MAL)

# Pero podemos entrar a la lista y cambiar un color:
mi_tupla[1][0] = "verde" 

# ¡Y hasta podemos agregar elementos a esa lista!
mi_tupla[1].append("amarillo")

print("Modificada:", mi_tupla)
