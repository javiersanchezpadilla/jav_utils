""" EL GRAN PROBLEMA DE PYTHON HILOS

    Pythno es un autentico GIL (Global Interpreter Lock), esto significa que
    el interprete de Python tiene una especie de cerrojo, y esto hace que un
    solo hilo por limitaciones del lenguaje solo puede ejecutar un código a la
    vez, lo que significa que si tratamos de trabajar con hilos al mismo tiempo
    en Python, no tienes paralelismo real, sino que tendrias algo como concurrencia
    secuencial, esto significa que para realizar una tarea con hilos

    Realiza una tarea                       *****    ****    *****
    Pasa a ejecuta otra tarea                   *****             *****
    de nuevo regresa a la tarea oriigal                  *****

    Y así todo el rato, en vez de utilizar ambas manos para clavar dos martillos,
    solo utiliza una para clavar los dos claves en tiempos distintos
    
    Solución. A partir de la versión "3.14t" de Python al momento de ejecutar se
    despliega el mensaje de free-threading, esto signfica que estamos usando una 
    versión sin la limitación de los GIL

    Las versiones FREE THREADING están disponibles desde la 3.13

        uv pip3 install 3.14t

    Instalarla con uv es mmuy sencillo
    """