""" Crear mapas de imágenes 
    Para este ejercicio se requiere el uso de la libreria folium.
    Se debe instalar con el comando: 
    
    $ pip3 install folium

    En google maps para obtenr la latitud y longitud de un lugar,
    se debe hacer click derecho en el lugar deseado y seleccionar "¿Qué hay aquí?".
    En la parte inferior de la pantalla aparecerá un cuadro con las coordenadas.
    En este caso se utilizarán las coordenadas del instituto Tecnológico de Acapulco
    Tambien se agregará un marcador en la ubicación del instituto.
"""

import folium

def generar_mapa():
    # The lines `latitud = 16.859646` and `longitud = -99.811233` are assigning specific latitude and
    # longitude coordinates to the variables `latitud` and `longitud`, respectively. In this case, the
    # coordinates `16.859646` and `-99.811233` correspond to the location of the Instituto Tecnológico
    # de Acapulco. These coordinates are used to center the map at that specific location when
    # creating the map using the Folium library in Python.
    latitud = 16.859646
    longitud = -99.811233

    mapa = folium.Map(location = [latitud, longitud], zoom_start=15)

    # Agregar un marcador en la ubicación del instituto
    folium.Marker(
        location=[latitud, longitud],
        popup="Instituto Tecnológico de Acapulco",
        tooltip="Clic aquí para más información"
        ).add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save("mapa.html")

generar_mapa()



