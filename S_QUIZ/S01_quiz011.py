"""
    Explanation: nums = [1, 2, 3, 4, 5] nums[-2::-2] 
    breaks down as: Start: -2 → index 3 → value 4 
    Stop: omitted → goes to the beginning 
    Step: -2 → move backwards by 2 Starting at 4, go backwards by 2: 4 → 2 → (end) 
    Result: [4, 2] 
    Key Concept: Negative step means reverse direction! Start at index -2 (value 4), 
    then jump backwards by 2 each time.
"""

numeros = [1, 2, 3, 4, 5]
resultado = numeros[-2::-2]

print(resultado)
