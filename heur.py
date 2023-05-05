
matrix = [[0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 1, 1,],
          [0, 0, 0, 0, 1, 1, 1,],
          [0, 0, 0, 0, 1, 1, 1,],
          [0, 0, 0, 0, 0, 0, 2,]]

# Posicion inicial
i = 0
j = 0

# Busqueda
while i < len(matrix):
    if matrix[i][j] == 1:
        i += 1
        j = max(j - 1, 0)  # Retroceder una celda, pero no más allá de la primera
    elif matrix[i][j] == 2:
        print("Encontrado en", i, j)
        break
    else:  # 0
        j += 1
