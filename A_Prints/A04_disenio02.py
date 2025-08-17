"""
    *
   * *
  *   *
 *     *
*********
"""

rows = 5
for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print(" " * (rows - i) + "*" * (2 * i - 1))
    else:
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")

