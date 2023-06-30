import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('ruta.jpg')

# Convertir la imagen a escala de grises
img_byn = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado a la imagen
img_suave = cv2.GaussianBlur(img_byn, (5, 5), 0)

# Aplicar detección de bordes utilizando
img_bordes = cv2.Canny(img_suave, 50, 150)

# Aplicar la transformada de Hough para detectar líneas
# es importante ir ajustando los parametros para el efecto deseado de deteccion
img_lineas = cv2.HoughLinesP(img_bordes, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# Dibujar las líneas encontradas sobre la imagen original
if img_lineas is not None:
    for linea in img_lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar la imagen con las líneas detectadas
cv2.imshow('Lineas detectadas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

