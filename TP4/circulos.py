import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('motor.jpg')
#imagen = cv2.imread('motor2.jpg')
#imagen = cv2.imread('motor3.jpg')

# Convertir la imagen a escala de grises
img_byn = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes utilizando el algoritmo de Canny
img_borde = cv2.Canny(img_byn, 50, 150)

# Aplicar la transformada de Hough para detectar círculos
#circulo = cv2.HoughCircles(img_borde, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=40, maxRadius=60)

circulo = cv2.HoughCircles(img_borde, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30, minRadius=50, maxRadius=75)
# Dibujar los círculos encontrados sobre la imagen original
if circulo is not None:
    circulo = np.round(circulo[0, :]).astype("int")
    for (x, y, r) in circulo:
        cv2.circle(imagen, (x, y), r, (0, 0, 255), 4)
        cv2.circle(imagen, (x, y), 2, (0, 255, 0), 6) #la coordenada del centro del circulo

# Mostrar la imagen con los círculos detectados


# Crea una ventana con el nombre deseado y el flag WINDOW_NORMAL
cv2.namedWindow('Circunferencia detectada', cv2.WINDOW_NORMAL)

# Especifica el tamaño deseado de la ventana (ancho, alto)
ventana = (800, 600)

# Ajusta el tamaño de la ventana
cv2.resizeWindow('Circunferencia detectada', ventana[0], ventana[1])

cv2.imshow('Circunferencia detectada', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()



