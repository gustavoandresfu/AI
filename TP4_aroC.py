import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread("imagen.jpg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# Aplicar detección de bordes utilizando Canny
edges = cv2.Canny(gray, 50, 150)

# Aplicar la transformada de Hough para detección de circunferencias
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Dibujar las circunferencias detectadas en la imagen original
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

# Mostrar la imagen original con las circunferencias detectadas
cv2.imshow("Detección de circunferencias", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
