def printEquiTriangle(rows):
   for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    
    print('*' * (2 * i + 1))
    
    
rows=5

printEquiTriangle(rows)

