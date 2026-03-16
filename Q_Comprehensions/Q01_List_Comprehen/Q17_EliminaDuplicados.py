""" Eliminar elementos duplicados de una lista """


lista = [1, 2, 2, 1, 1, 4, 5]


duplicados=[]

#obtiene los elementos que se repiten en la lista y los elimina mediante, una vez eliminado n elemento, vuelve aidar otro (diplucaios)
#recorrido a la lista y seguir buscando hasta que ya no haya duplicados
[duplicados.append(x) for x in lista if x not in duplicados] 
print(duplicados)                                      
