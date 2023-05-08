
espacio = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1,],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],]

# Posicion inicial
i = 0
j = 0

# Busqueda
while i < len(espacio):

    print(f"({i},{j})",end = ' ')
    if espacio[i][j] == 1:
        i += 1
        j = max(j - 1, 0)  # Retroceder una celda, pero no más allá de la primera
        
    elif espacio[i][j] == 2:
        print("Objetivo encontrado en coordenada ", i, j)
        break
    else:  # 0
        j += 1
