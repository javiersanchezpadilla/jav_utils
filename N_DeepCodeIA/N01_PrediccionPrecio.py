""" Cuanto cuesta un piso de 135 m2
    Lo vamos a predecir con un modelo de ML
    Usando sklearn
    El modelo se entreno con 1000 datos
    
    Instalamos sklearn
    pip3 install scikit-learn

    Esto es como tener una calculadora de regresion lineal
    que aprenda de los datos que le damos
    x = metros cuadrados
    y = precio del piso (por cada elemento de x se tiene un elemento de y)
"""

from sklearn.linear_model import LinearRegression

x = [[70], [80], [90], [100], [110], [120]]
y = [155000, 165000, 180000, 190000, 200000, 210000]

modelo = LinearRegression()
modelo.fit(x, y)

metros = [[135]]
prediccion = modelo.predict(metros)

print(f"Precio estimado {int(prediccion[0])}")

