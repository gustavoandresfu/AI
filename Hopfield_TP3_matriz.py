import numpy as np
patron_circular = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def entrenar_hopfield(patron_circular):
    num_pixels = patron_circular.size

    # Inicializar la matriz de pesos sinápticos
    pesos = np.zeros((num_pixels, num_pixels))

    # Actualizar los pesos sinápticos
    for i in range(num_pixels):
        for j in range(num_pixels):
            if i != j:
                pesos[i, j] += patron_circular[i] * patron_circular[j]

    return pesos

# Entrenar el modelo de Hopfield
pesos = entrenar_hopfield(patron_circular.flatten())#lo vectorizamos


def actualizar_estado_neu(pesos, n_estado):
    num_neurons = n_estado.size

    # Actualizar el estado de cada neurona según la regla de actualización de Hopfield
    for i in range(num_neurons):
        n_estado[i] = np.sign(np.dot(pesos[i, :], n_estado))

    return n_estado

def identificar_patron(imagen, pesos):
    n_estado = imagen.copy()
    intera = 0

    # Iterar hasta que los estados de las neuronas converjan o hasta alcanzar el
    #  número máximo de iteraciones (100)
    while intera < 100:
        previo_estado = n_estado.copy()
        n_estado = actualizar_estado_neu(pesos, n_estado)
        # Comprobar si los estados de las neuronas han convergido
        if np.array_equal(n_estado, previo_estado):
            break

        intera += 1
    
    return n_estado

# Identificar el patrón desconocido
patron_entrada = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

patron_entrada2 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

limpiar_patron_circular = identificar_patron(patron_entrada.flatten(), pesos)
limpiar_patron_circular = limpiar_patron_circular.reshape(patron_entrada.shape)

limpiar_patron_circular2 = identificar_patron(patron_entrada2.flatten(), pesos)
limpiar_patron_circular2 = limpiar_patron_circular2.reshape(patron_entrada2.shape)

# Imprimir el patrón original y el patrón reconstruido y limpio
# Doy dos salidas para interpretar los resultados
print("Patrón entrada 1:")
print(patron_entrada)

print("Patrón limpio:")
print(limpiar_patron_circular)

print("Patrón entrada 2:")
print(patron_entrada2)

print("Patrón limpio:")
print(limpiar_patron_circular2)
