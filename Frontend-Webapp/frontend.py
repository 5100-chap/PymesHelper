import streamlit as st
import cv2
import os
import dotenv
from time import sleep
from Camera.CameraLogic import VideoTransformer
from Camera.CameraProcessor import CameraProcessor
from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoHTMLAttributes

# Cargar variables de entorno
dotenv.load_dotenv()

# Configuración de la página
st.set_page_config(page_title="Prueba de Contorno de Cámara")
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2E86C1;
    }
    .description {
        font-size: 18px;
        color: #FFFFFF97;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="title">Clasificación de Video PymesHelper</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="description">Prueba de Contorno de Cámara</div>',
    unsafe_allow_html=True,
)

# Espacios reservados para mostrar el video y la clasificación
frame_placeholder = st.empty()
classification_box = st.empty()

frame_count = 0
frame = None
# Inicializar el procesador de cámara con la URL de la API
api_url = os.getenv("API_URL")
camera_processor = CameraProcessor(api_url=api_url)

# Configurar el streamer de WebRTC
webrtc_ctx = webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=lambda: VideoTransformer(camera_processor=camera_processor),
    media_stream_constraints={
        "video": {
            "width": {"ideal": 1920},
            "height": {"ideal": 1080},
            "frameRate": {"ideal": 20}
        },
        "audio": False
    },
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
            if webrtc_ctx.video_processor.last_processed_frame is not None:
                frame = webrtc_ctx.video_processor.last_processed_frame

            if frame is not None:
                # Convertir el frame a formato ndarray
                img = frame

                # Enviar el frame a la API para obtener la clasificación
                classification = camera_processor.send_video(img)

                # Procesar el frame para dibujar contornos
                # processed_frame = camera_processor.process_frame(img)

                # Mostrar la clasificación
                classification_box.text_area(
                    "El modelo detectó que esto es:",
                    value=classification,
                    height=100,
                    key=f"classification_{frame_count}",
                )
                frame_count += 1

        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")
            break
