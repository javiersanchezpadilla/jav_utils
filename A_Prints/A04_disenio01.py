"""
    1
   12
  123
 1234
12345
"""


rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "". join(str(j) for j in
range (1, i + 1)))