""" ANSWER: A) heo HELLO 

    Explanation: 
    x = "hello" - x starts as "hello" 
    y = x.replace("l", "") - removes all "l"s, so 
    y = "heo" (x stays "hello") x = x.upper() - 
    converts x to uppercase, so x = "HELLO" 
    Prints y first (heo), then x (HELLO) 
    Key Concept: Strings are immutable in Python! 
    Methods like replace() and upper() don't modify the original string
    they return a NEW string. Did you get it right? """


x = "hello"
y = x.replace('l', "")
x = x.upper()

print(y, x) # Resultado heo HELLO
