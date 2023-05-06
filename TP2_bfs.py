from collections import deque

def bfs(espacio, nodo_inicial, objetivo):
    cola = deque([nodo_inicial])
    visitado = set()

    while cola:
        nodo = cola.popleft()

        if nodo in visitado:
            continue

        visitado.add(nodo)
        print({nodo});
        if espacio[nodo[0]][nodo[1]] == objetivo:
            return nodo

        adyacentes = ver_adyacentes(nodo, espacio)
        for vecino in adyacentes:
            if vecino not in visitado:
                cola.append(vecino)

    return None

def ver_adyacentes(nodo, espacio):
    row, col = nodo
    rows = len(espacio)
    cols = len(espacio[0])

    adyacentes = []

    # check der vecino
    if col + 1 < cols:
        adyacentes.append((row, col + 1))

    # check izq vecino
    if col - 1 >= 0:
        adyacentes.append((row, col - 1))

    # check abajo vecino
    if row + 1 < rows:
        adyacentes.append((row + 1, col))

    # check arriba vecino
    if row - 1 >= 0:
        adyacentes.append((row - 1, col))

    return adyacentes

espacio = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

nodo_inicial = (4, 6)
objetivo = 2

resultado = bfs(espacio, nodo_inicial, objetivo)

if resultado:
    print(f"El objetivo fue encontrado en  coordenadas: {resultado}")
else:
    print("El objetivo no fue encontrado")
    """""
    hola
    """""