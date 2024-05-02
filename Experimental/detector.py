import cv2
import numpy as np

# Iniciar la captura de video desde la webcam
cap = cv2.VideoCapture(0)

# Crear ventanas para mostrar los resultados
cv2.namedWindow('Imagen original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Objetos circulares/elípticos con color detectado', cv2.WINDOW_NORMAL)

while True:
    # Leer un frame de la webcam
    ret, frame = cap.read()
    frame_blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    # Convertir el frame a espacio de color HSV
    hsv = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2HSV)

    # Definir los rangos de colores que se quieren detectar
    lower_bound = np.array([0, 60, 0])
    upper_bound = np.array([179, 255, 255])

    # Crear una máscara que incluya solo los colores dentro del rango
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Encontrar los contornos en la máscara binaria
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una imagen negra para dibujar los contornos
    contoured_image = np.zeros_like(frame)

    # Variable para verificar si se detectó un objeto en la mitad derecha
    object_detected = False

    # Filtrar y dibujar solo los contornos que son circulares o elípticos
    for contour in contours:
        if cv2.contourArea(contour) > 600:
            perimeter = cv2.arcLength(contour, True)
            circularity = 4 * np.pi * cv2.contourArea(contour) / (perimeter ** 2)
            object_detected=True

            # if 0.7 <= circularity <= 1.2:
            cv2.drawContours(contoured_image, [contour], -1, (0, 255, 0), 2)

            #     # Calcular el centroide del contorno
            #     M = cv2.moments(contour)
            #     if M["m00"] != 0:
            #         cX = int(M["m10"] / M["m00"])
            #         cY = int(M["m01"] / M["m00"])
                    
            #         # Verificar si el centroide está en la mitad derecha de la pantalla
            #         if cY< frame.shape[1] / 2:
            #             object_detected = True

    # Si se detectó un objeto en la mitad derecha, enviar '1' al servo
    if object_detected:
        print(f'Detected')
    else:
        print(f'Undetected')

    # Mostrar el resultado y la imagen original
    cv2.imshow('Imagen original', frame)
    cv2.imshow('Objetos circulares/elípticos con color detectado', contoured_image)

    # Esperar a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
