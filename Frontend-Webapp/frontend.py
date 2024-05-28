import cv2
import numpy as np
import streamlit as st
import base64
import requests
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()

# Propiedades de la página de streamlit
st.set_page_config(page_title="Camera Contour Test")
st.write("Clasificación de Video PymesHelper")
frame_placeholder = st.empty()
response_placeholder = st.empty()

def send_video(frame, ext='jpg'):
    try:
        # Encode the video in base64
        _, video_data = cv2.imencode(f".{ext}", frame)
        video_bytes = base64.b64encode(video_data)

        # Get the API URL from environment variable
        api_url = os.getenv("API_URL")

        if api_url:
            # Send the video to the API
            url = api_url + "/classify_video"
            response = requests.post(url, data=video_bytes)

            # Get the classification from the response
            classification = response.json()["classification"]
        else:
            classification = "API URL not defined"

        return classification
    except Exception as e:
        return str(e)

# Lista las camaras disponibles e intenta abrir cada una
def list_cameras():
    available_cameras = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

# Search for available cameras
cameras = list_cameras()

if len(cameras) == 0:
    st.error("No cameras found.")
else:
    # Allow user to select a camera
    selected_camera = st.selectbox("Select a camera", cameras)
    
    if selected_camera is not None:
        if st.button("Empezar", key="start_button"):
            # Initialize the selected camera
            cap = cv2.VideoCapture(selected_camera)

            if not cap.isOpened():
                st.error(f"Failed to open camera {selected_camera}.")
            else:
                stop_processing = False
                
                stop_button = st.button("Parar", key="stop_button")
                
                while not stop_processing:
                    try:
                        # Leer un frame de la cámara seleccionada
                        ret, frame = cap.read()

                        # Si se pudo leer el frame
                        if ret:
                            # Enviar el frame a la API para clasificación
                            classification = send_video(frame)

                        frame_blurred = cv2.GaussianBlur(frame, (5, 5), 0)

                        # Convert frame to HSV color space
                        hsv = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2HSV)

                        # Define color ranges
                        lower_bound = np.array([0, 60, 0])
                        upper_bound = np.array([179, 255, 255])

                        # Create a mask with only the colors in range
                        mask = cv2.inRange(hsv, lower_bound, upper_bound)

                        # Find contours from the binary mask
                        contours, _ = cv2.findContours(
                            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
                        )

                        # Filter contours
                        for contour in contours:
                            if cv2.contourArea(contour) > 300:
                                perimeter = cv2.arcLength(contour, True)
                                circularity = (
                                    4 * np.pi * cv2.contourArea(contour) / (perimeter**2)
                                )

                                if circularity <= 2.5:
                                    # Calculate the centroid
                                    M = cv2.moments(contour)
                                    if M["m00"] != 0:
                                        cX = int(M["m10"] / M["m00"])
                                        cY = int(M["m01"] / M["m00"])

                                    # Check if the centroid is on the right half of the screen
                                    if cY < frame.shape[1] / 2:
                                        response_placeholder.write(
                                            f"## {send_video(frame=frame, ext='png')}"
                                        )
                                        cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)

                        # Mostrar el frame con los objetos detectados
                        frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")
                        st.write(f"Clasificación: {classification}")
                        
                        if stop_button:
                            stop_processing = True
                            
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
                        break
                        
                cap.release()
