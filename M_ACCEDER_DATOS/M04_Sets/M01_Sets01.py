""" MANEJO DE CONJUNTOS.

   Los conjuntos (sets) en Python son colecciones desordenadas, mutables y sin 
   elementos duplicados, ideales para eliminar duplicados y realizar 
   operaciones matemáticas como unión, intersección y diferencia. Se crean 
   usando llaves {} o set(), y son eficientes para búsquedas de elementos únicos. 

   Creación y Características
   --------------------------
   A) Creación: mi_set = {1, 2, 3, 3} resulta en {1, 2, 3} (elimina duplicados 
      automáticamente).
   B) Set vacío: Se debe usar set(), ya que {} crea un diccionario vacío.
   C) Mutable: Se pueden añadir o eliminar elementos, pero estos deben ser 
      inmutables (ej. números, cadenas, tuplas).
   D) Desordenados: No tienen un índice definido y no admiten indexación. 

    La Analogía: La Bolsa de Dulces Mágica
    --------------------------------------
    Imagina que tienes una bolsa donde guardas dulces. Pero esta bolsa tiene dos 
    reglas:
    A) No acepta repetidos: Si intentas meter dos caramelos de fresa idénticos, 
       la bolsa "fusiona" el segundo con el primero. Solo queda uno.
    B) No hay orden: Los dulces saltan dentro de la bolsa todo el tiempo. 
       No importa cuál metiste primero, cuando metes la mano, no sabes cuál sacarás.

1. ¿Cómo se crea un conjunto?
Usamos llaves { }. Nota que, a diferencia de las listas, aquí no hay duplicados."""

# Creamos un conjunto con elementos repetidos
mi_bolsa = {"Fresa", "Menta", "Fresa", "Chocolate", "Menta"}

# Al imprimirlo, Python habrá eliminado los repetidos automáticamente
print(mi_bolsa) 
# Resultado: {'Menta', 'Chocolate', 'Fresa'} (el orden puede variar)