# Usando f-string
print(f'[{chr(65)}]')  # Output: [A]
print(f'[{chr(66)}]')  # Output: [B]

# Usando el método str.format
print('[{}]'.format(chr(65)))  # Output: [A]
print('[{}]'.format(chr(66)))  # Output: [B]

# Usando la funcion format con placeholders
print('[{:c}]'.format(65))  # Output: [A]  
print('[{:c}]'.format(66))  # Output: [B]

# Usando concatención con la finción chr
print('[' + chr(65) + ']')  # Output: [A]
print('[' + chr(66) + ']')  # Output: [B]

# Usando el estilo del formateo de la cadena de caracteres
print('[%c]' % 65)  # Output: [A]
print('[%c]' % 66)  # Output: [B]
