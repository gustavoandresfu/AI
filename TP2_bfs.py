from collections import deque

def bfs(grafo, objetivo):
    cola = deque(["B1"])
    visitado = set()

    while cola:
        nodo = cola.popleft()

        if nodo in visitado:
            continue

        visitado.add(nodo)
        print(" -> " + nodo , end = ' ')  # Imprimo el nodo para conocer el avance
        if nodo == objetivo:
            return nodo

        adyacentes = grafo[nodo]
        for vecino in adyacentes:
            if vecino not in visitado:
                cola.append(vecino)

    return None

grafo = {
    "B1": ["B2"],
    "B2": ["B1", "B3"],
    "B3": ["B2", "B4"],
    "B4": ["B3", "B5"],
    "B5": ["B4", "B6"],
    "B6": ["B5", "B7"],
    "B7": ["B6", "B8"],
    "B8": ["B7", "A1"],
    "A1": ["B8", "B10"], #aqui pongo el objetivo a encontrar
    "B10": ["A1"]
}

objetivo = "A1"

resultado = bfs(grafo,  objetivo)

if resultado:
    print(f"\n El objetivo fue encontrado en el nodo: {resultado}")
else:
    print("El objetivo no fue encontrado")
