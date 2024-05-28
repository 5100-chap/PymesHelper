import streamlit as st
import cv2
import os
import dotenv
from Camera.CameraLogic import VideoTransformer
from Camera.CameraProcessor import CameraProcessor
from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoHTMLAttributes

# Cargar variables de entorno
dotenv.load_dotenv()

# Configuración de la página
st.set_page_config(page_title="Prueba de Contorno de Cámara")
st.write("Clasificación de Video PymesHelper")

# Espacios reservados para mostrar el video y la clasificación
frame_placeholder = st.empty()
classification_box = st.empty()

# Contador de frames
frame_count = 0

# Inicializar el procesador de cámara con la URL de la API
api_url = os.getenv("API_URL")
camera_processor = CameraProcessor(api_url=api_url)

# Configurar el streamer de WebRTC
webrtc_ctx = webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=lambda: VideoTransformer(camera_processor=camera_processor),
    media_stream_constraints={"video": True, "audio": False},
    video_html_attrs=VideoHTMLAttributes(
        autoPlay=True,
        controls=False,
        style={"width": "100%"},
    ),
)

# Procesar el video en tiempo real
if webrtc_ctx.video_processor:
    webrtc_ctx.video_processor.camera_processor = camera_processor

    while True:
        try:
            frame = webrtc_ctx.video_processor.recv()

            if frame is not None:
                # Convertir el frame a formato ndarray
                img = frame.to_ndarray(format="bgr24")

                # Enviar el frame a la API para obtener la clasificación
                classification = camera_processor.send_video(img)
                
                # Procesar el frame para dibujar contornos
                processed_frame = camera_processor.process_frame(img)

                # Mostrar el frame procesado y la clasificación
                frame_placeholder.image(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB), channels="RGB")
                classification_box.text_area("El modelo detectó que esto es:", value=classification, height=100, key=f"classification_{frame_count}")
                frame_count += 1

        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")
            break

        if st.button("Parar", key="stop_button"):
            break