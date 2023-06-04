import cv2
import numpy as np

# Cargar la imagen en color
image = cv2.imread("imagen.jpg", cv2.IMREAD_COLOR)

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de mediana a la imagen en escala de grises
filtered_image = cv2.medianBlur(gray_image, 5)

# Aplicar la detección de círculos utilizando la transformada de Hough
circles = cv2.HoughCircles(filtered_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=5, maxRadius=30)

if circles is not None:
    # Convertir las coordenadas de los círculos a enteros
    circles = np.uint16(np.around(circles))

    for circle in circles[0, :]:
        # Obtener las coordenadas y el radio del círculo
        x, y, radius = circle

        # Dibujar el círculo en la imagen original en color rojo (BGR)
        cv2.circle(image, (x, y), radius, (0, 0, 255), 2)

        # Dibujar el centro del círculo en la imagen original en color rojo (BGR)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

        # Mostrar las coordenadas x e y del centro del círculo
        print("Coordenadas del centro del aro:")
        print("x:", x)
        print("y:", y)

    # Mostrar la imagen con los círculos detectados
    cv2.imshow("Círculos detectados", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se encontraron círculos en la imagen")

#how can i split a string?
input_string=input("enter string: ")
li=input_string.split()
print("".join(li),"this is the joined string")







