""" Para este ejemplo, se requiere instalar la librería google
pip3 install google 

Existe una version más reciente de la librería llamada google-search, 
la cual permite limitar el número de resultados
pip3 install google-search
"""

from googlesearch import search

busqueda = input("Ingrese su búsqueda: ")

for resultado in search(busqueda): #, num_results=10): si usamos google-search
     print(resultado)




# para este ejemplo se requiere instalar la librería google-search
# def buscar_en_google(consulta, num_resultados=10):
#     """
#     Realiza una búsqueda en Google y devuelve los enlaces de los resultados.
    
#     :param consulta: La consulta de búsqueda.
#     :param num_resultados: Número de resultados a devolver.
#     :return: Lista de URLs de los resultados de búsqueda.
#     """
#     resultados = []
#     try:
#         for url in search(consulta, num_results=num_resultados):
#             resultados.append(url)
#     except Exception as e:
#         print(f"Error al realizar la búsqueda: {e}")
    
#     return resultados

# # Ejemplo de uso
# if __name__ == "__main__":
#     consulta = "Python programming"
#     num_resultados = 5
    
#     resultados = buscar_en_google(consulta, num_resultados)
#     print(f"Resultados de búsqueda para '{consulta}':")
#     for i, url in enumerate(resultados, start=1):
#         print(f"{i}. {url}")

