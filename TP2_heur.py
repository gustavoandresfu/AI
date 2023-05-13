from collections import deque

def bfs(grafo, nodo_inicial, objetivo):
    cola = deque([nodo_inicial])
    visitado = set()

    while cola:
        nodo = cola.popleft()

        if nodo in visitado:
            continue
        visitado.add(nodo)
       
        print(" -> " +nodo  , end = ' ')  # Imprimo el nodo para conocer el avance
        if nodo == objetivo:
            return nodo

        adyacentes = grafo[nodo]
        for vecino in adyacentes:
            if vecino not in visitado:
                cola.append(vecino)

    return None
def heuristica(distancia_estimada, cantidad_nodos):
    return cantidad_nodos - (cantidad_nodos // distancia_estimada)

grafo = {
    "1": ["2"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["3", "5"],
    "5": ["4", "6"],
    "6": ["5", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"], #aqui pongo el objetivo a encontrar
    "10": ["9"]
}

# de alguna manera tengo que fijar el objetivo
objetivo = "4"  
# la distancia estimada de  la posicion  desde el borde
distancia_estimada = 4 
#Elijo donde iniciar el recorrido la funcion heuristica
# me dice donde me posiciono con posibilidades de mayor exito

nodo_inicial = str(heuristica(2,len(grafo))) 
print("Nodo de inicio: "+nodo_inicial)

#corro la funcion bfs, desde el nodo elegido
resultado = bfs(grafo, nodo_inicial, objetivo)

if resultado:
    print(f"\n El objetivo fue encontrado en el nodo: {resultado}")
else:
    print("El objetivo no fue encontrado")
