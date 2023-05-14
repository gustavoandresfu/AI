from collections import deque

def bfs(grafo, nodo_inicial, objetivo):
    cola = deque([nodo_inicial])
    visitado = set()

    while cola:
        nodo = cola.popleft()

        if nodo in visitado:
            continue
        visitado.add(nodo)

        print(" -> " + str(nodo), end=' ')  # Imprimo el nodo para conocer el avance
        if nodo == objetivo:
            return nodo

        adyacentes = grafo[nodo]
        for vecino in adyacentes:
            if vecino not in visitado:
                cola.append(vecino)

    return None

def heuristica(distancia_minima, distancia_maxima):
    return (distancia_maxima + distancia_minima) // 2


grafo = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10], 
    10: [9]
}


# la distancia estimada minima y maxima al objetivo
distancia_minima = 6
distancia_maxima = 8

#busco con la funcion el nodo ideal para iniciar busqueda
nodo_inicial = heuristica(distancia_minima, distancia_maxima) 

for i in range(6, 9): #el rango corresponde a la ventana de movimiento del objetivo
    objetivo = i # de alguna manera tengo que fijar el objetivo
    print("Nodo de inicio: " + str(nodo_inicial))
    # corro la función bfs, desde el nodo elegido
    resultado = bfs(grafo, nodo_inicial, objetivo)
    if resultado:
        print(f"\nEl objetivo fue encontrado en el nodo: {resultado}")
    else:
        print("El objetivo no fue encontrado") 