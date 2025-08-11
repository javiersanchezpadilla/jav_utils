""" Este ejemplo muestra el uso de la clase Thread de la librería threading
"""

# The lines `import threading`, `import time`, `import requests`, and `import os` are importing
# necessary modules in Python for the functionality of the script. Here's what each import statement
# does:
import threading
import time
import requests 
import os

paginas = [
    'https://acapulco.tecnm.mx/wp-content/uploads/carreras/licenciatura_en_administracion/Materias/2/funcion_administrativa_i.pdf',
    'https://acapulco.tecnm.mx/wp-content/uploads/carreras/licenciatura_en_administracion/Materias/2/dinamica_social.pdf',
    'https://acapulco.tecnm.mx/wp-content/uploads/carreras/licenciatura_en_administracion/Materias/2/derecho_empresarial.pdf',
    'https://acapulco.tecnm.mx/wp-content/uploads/carreras/licenciatura_en_administracion/Materias/2/costos_de_manufactura.pdf',
]


def descargar_pagina(url):
    nombre_archivo = os.path.basename(url)
    print(f"Descargando {nombre_archivo}...")

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa

        with open(nombre_archivo, 'wb') as f:
            f.write(respuesta.content)

        print(f"{nombre_archivo} descargado correctamente.")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")


def main():
    inicio = time.time()
    hilos = []
    print("Iniciando descargas...")

    for pagina in paginas:
        hilo = threading.Thread(target=descargar_pagina, args=(pagina,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()  # Espera a que todos los hilos terminen

    fin = time.time()
    duracion = fin - inicio
    print(f"Descargas completadas en {duracion:.2f} segundos.")

if __name__ == "__main__":
    main()