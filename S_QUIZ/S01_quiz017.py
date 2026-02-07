""" ANSWER: [1, 0, 1, 0] 

    Explanation: 
    x = [0] * 2 → x = [0, 0] 
    x[0] = 1 → x = [1, 0] 
    y = x * 2 → duplicates the list: [1, 0, 1, 0] 
    
    Result: [1, 0, 1, 0] 
    
    Key Concept: The * operator repeats the current contents of the list. 
    After modifying x to [1, 0], multiplying by 2 creates [1, 0, 1, 0]!"""


x = [0] * 2
x[0] = 1
y = x * 2

print(y)    # [1, 0, 1, 0]
