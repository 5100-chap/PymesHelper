import streamlit as st
import cv2
import time
import dotenv
import os
from Camera.CameraLogic import CameraLogic
from Camera.CameraProcessor import CameraProcessor

dotenv.load_dotenv()

st.set_page_config(page_title="Prueba de Contorno de Cámara")
st.write("Clasificación de Video PymesHelper")
frame_placeholder = st.empty()
response_placeholder = st.empty()
classification_box = st.empty()
frame_count = 0

camera_logic = CameraLogic()
camera_processor = CameraProcessor(api_url=os.getenv("API_URL"))

cameras = camera_logic.list_cameras()

if len(cameras) == 0:
    st.error("No se encontraron cámaras.")
else:
    selected_camera = st.selectbox("Selecciona una cámara", cameras)
    
    if selected_camera is not None:
        if st.button("Empezar", key="start_button"):
            cap = cv2.VideoCapture(selected_camera)

            if not cap.isOpened():
                st.error(f"No se pudo abrir la cámara {selected_camera}.")
            else:
                stop_processing = False
                
                stop_button = st.button("Parar", key="stop_button")
                ##save_button = st.button("Guardar resultados")
                
                while cap.isOpened() and not stop_processing:
                    try:
                        ret, frame = cap.read()

                        if ret:
                            classification = camera_processor.send_video(frame)
                            processed_frame = camera_processor.process_frame(frame)

                        frame_placeholder.image(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB), channels="RGB")
                        classification_box.text_area("El modelo detectó que esto es:", value=classification, height=100, key=f"classification_{frame_count}")
                        frame_count += 1
                        
                        if stop_button:
                            stop_processing = True
                        
                        ##if save_button:
                        ##    with open("resultados.txt", "w") as file:
                        ##        file.write(classification)
                        ##    st.success("Resultados guardados en resultados.txt")
                            
                    except Exception as e:
                        st.error(f"Ocurrió un error: {str(e)}")
                        break
                        
                cap.release()
                
                new_selected_camera = st.selectbox("Selecciona una nueva cámara", cameras, key="new_camera")
                selected_camera = new_selected_camera
                
                time.sleep(5)
                st.experimental_rerun()
