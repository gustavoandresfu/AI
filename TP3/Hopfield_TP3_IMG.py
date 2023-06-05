import cv2
import numpy as np


# Función para cargar una imagen y convertirla en una matriz binaria
def cargar_imagen_ruta(ruta_imagen):
    imagen = cv2.imread(ruta_imagen, 0)  # Cargar imagen en escala de grises
    imagen = cv2.resize(imagen, (70, 70))
    _, imagen_binaria = cv2.threshold(imagen, 128, 1, cv2.THRESH_BINARY)  # Convertir a binario (0 o 1)
    
    return imagen_binaria

# Función para convertir una matriz en una imagen
def matriz_a_imagen(matriz):
    imagen = np.uint8(matriz * 255)  # Convertir la matriz binaria (0 o 1) a 8 bits (0 o 255)
    return imagen

# Función para entrenar el modelo de Hopfield con una imagen
def entrenar_hopfield(imagen):
    num_pixels = imagen.size

    # Inicializar la matriz de pesos sinápticos
    pesos = np.zeros((num_pixels, num_pixels))

    # Actualizar los pesos sinápticos
    for i in range(num_pixels):
        for j in range(num_pixels):
            if i != j:
                pesos[i, j] += imagen[i] * imagen[j]

    return pesos

# Función para actualizar el estado de las neuronas según la regla de actualización de Hopfield
def actualizar_estado_neu(pesos, n_estado):
    num_neurons = n_estado.size

    # Actualizar el estado de cada neurona según la regla de actualización de Hopfield
    for i in range(num_neurons):
        n_estado[i] = np.sign(np.dot(pesos[i, :], n_estado))

    return n_estado

# Función para identificar un patrón desconocido en una imagen
def identificar_patron(imagen, pesos):
    n_estado = imagen.copy()
    intera = 0

    # Iterar hasta que los estados de las neuronas converjan o hasta alcanzar el
    # número máximo de iteraciones (100)
    while intera < 100:
        previo_estado = n_estado.copy()
        n_estado = actualizar_estado_neu(pesos, n_estado)
        # Comprobar si los estados de las neuronas han convergido
        if np.array_equal(n_estado, previo_estado):
            break

        intera += 1

    return n_estado

# Ruta de la imagen de patrón  de entrada
ruta_patron_entrada = "TP3/Original/imagen_motor.jpg"

# Cargar imagen de patrón  de entrada y convertirla en una matriz
patron_entrada = cargar_imagen_ruta(ruta_patron_entrada)

# Entrenar el modelo de Hopfield con la imagen del patrón 
pesos = entrenar_hopfield(patron_entrada.flatten())

# Ruta de la imagen de patrón desconocido
ruta_patron_desconocido =  "TP3/Muestras/imagen_zoom.jpg"
#ruta_patron_desconocido = "TP3/Muestras/imagen_abajo_der.jpg"
#ruta_patron_desconocido = "TP3/Muestras/imagen_arriba_izq.jpg"
#ruta_patron_desconocido = "TP3/Muestras/imagen_perfiljpg"
#ruta_patron_desconocido = "TP3/Muestras/imagen_zoom.jpg"

#Estas imagenes no se encuentra el patron:

#ruta_patron_desconocido = "TP3/Muestras/imagen_negro.jpg"
#ruta_patron_desconocido = "TP3/Muestras/imagen_blanco.jpg"
#ruta_patron_desconocido = "TP3/Muestras/imagen_arriba_izq_sin_luz.jpg"


# Cargar imagen de patrón desconocido y convertirla en una matriz
patron_desconocido = cargar_imagen_ruta(ruta_patron_desconocido)

# Identificar el patrón desconocido
patron_limpiado = identificar_patron(patron_desconocido.flatten(), pesos)
patron_limpiado = patron_limpiado.reshape(patron_desconocido.shape)

# Convertir las matrices en imágenes para visualización
patron_entrada_imagen = matriz_a_imagen(patron_entrada)
patron_limpiado_imagen = matriz_a_imagen(patron_limpiado)

# Mostrar las imágenes

cv2.imshow("Patron de entrada", patron_entrada_imagen)
cv2.resizeWindow("Patron de entrada", 300, 300)
cv2.imshow("Patron limpio en imagen", patron_limpiado_imagen)
cv2.resizeWindow("Patron limpio en imagen", 300, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()









