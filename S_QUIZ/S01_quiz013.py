"""
    Cuando i = 1: El while corre 1 vez (j=0). Suma 0
    Cuando i = 2: El while corre 2 veces (j=0, j=1). Suma 0 + 1
    Cuando i = 3: El while corre 3 veces (j=0, j=1, j=2). Suma 0 + 1 + 2
    Cuando i = 4: El while corre 4 veces (j=0, j=1, j=2, j=3). Suma 0 + 1 + 2 + 3
    
    Resultado final: 0 + 0 + 1 + 0 + 1 + 2 + 0 + 1 + 2 + 3 = 10.
"""

resultado = 0
for i in range(1, 5):
    j = 0
    while j < i:
        resultado += j
        j += 1
    j
print(resultado)
