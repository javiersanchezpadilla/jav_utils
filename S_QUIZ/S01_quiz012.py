""" En este ejemplo se muestra como resultados solo los archivos
    que terminan (.endswith()) con .csv o .pdf

    Resultado: ['data.csv', 'report.pdf']
"""

archivos = ['data.csv', 'photo.png', 'report.pdf', 'notes.txt']

print([f for f in archivos if f.endswith(('.csv', '.pdf'))])
