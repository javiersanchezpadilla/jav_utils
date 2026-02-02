"""
    ANSWER: [2, 4, 6] 
    Explanation: The list comprehension flattens the matrix and filters even 
    numbers for row in matrix → iterates through [1, 2], [3, 4], [5, 6] 
    for x in renglon → gets each individual number 
    if x % 2 == 0 → keeps only even numbers Process: 1❌, 2✅, 3❌, 4✅, 5❌, 6✅ 
    Result: [2, 4, 6] 
    🔑 Key Concept: Nested list comprehensions flatten nested structures! 
    The order is [expression FOR outer FOR inner IF condition] Did you get it right?

    Canal TikTok onelinerio
"""
# matrix de 3 renglones por dos columnas
matrix = [[1, 2], [3, 4], [5, 6]]

resultado = [x for renglon in matrix
             for x in renglon
             if x % 2 == 0 ] 

print(resultado)
