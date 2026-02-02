""" ANSWER: A) 14

    Explanation:
    func(*[2, 3], 4) unpacks the list
    This becomes: func(2, 3, 4)
    So: a=2, b=3, c=4
    Calculate: a + b * c → 2 + 3 * 4 → 2 + 12 = 14
    Result: 14
    Key Concept: The * operator unpacks iterables as positional arguments. 
    *[2, 3] becomes two separate arguments, then 4 is the third!
"""

def funcion(a, b, c):
    return a + b * c


resultado = funcion(*[2, 3], 4)
print(resultado)
