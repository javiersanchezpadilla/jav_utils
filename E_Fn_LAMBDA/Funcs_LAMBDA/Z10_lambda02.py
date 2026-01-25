""" ¿Para qué sirven realmente? (El poder de map)
    Las lambdas brillan cuando se usan con otras funciones como map(), 
    que aplica una regla a toda una lista.

    Ejemplo: Tienes una lista de números y quieres multiplicarlos todos por 2."""

numeros = [1, 2, 3, 4]

                                        # map(regla_lambda, lista_a_procesar)
                                        # (Usamos list() porque map devuelve un objeto 
                                        # especial que necesita ser convertido a 
                                        # lista para leerse).
dobles = list(map(lambda x: x * 2, numeros))

print(dobles)                           # [2, 4, 6, 8]
