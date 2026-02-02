""" ANSWER: None 

    Explanation: 
    d.get('c', []) → key 'c' doesn't exist, so returns default value [] 
    (new empty list) [].append(3) → modifies the list to [3], but 
    .append() returns None! result = None 
    Result: None
    Key Concept: The .append() method modifies a list in-place and always 
    returns None, not the modified list. This catches many developers off 
    guard!"""


d = {'a':1, 'b':2}
resultado = d.get('c', []).append(3)

print(resultado)
