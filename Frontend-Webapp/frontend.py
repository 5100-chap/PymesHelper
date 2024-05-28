import streamlit as st
import cv2
import time
import dotenv
import os
from Camera.CameraLogic import VideoTransformer
from Camera.CameraProcessor import CameraProcessor
from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoHTMLAttributes


dotenv.load_dotenv()

st.set_page_config(page_title="Prueba de Contorno de Cámara")
st.write("Clasificación de Video PymesHelper")
frame_placeholder = st.empty()
response_placeholder = st.empty()
classification_box = st.empty()
frame_count = 0

camera_processor = CameraProcessor(api_url=os.getenv("API_URL"))

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

if webrtc_ctx.video_processor:
    webrtc_ctx.video_processor.camera_processor = camera_processor

    while True:
        try:
            frame = webrtc_ctx.video_processor.recv()

            if frame is not None:
                classification = camera_processor.send_video(frame.to_ndarray(format="bgr24"))
                processed_frame = camera_processor.process_frame(frame.to_ndarray(format="bgr24"))

                frame_placeholder.image(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB), channels="RGB")
                classification_box.text_area("El modelo detectó que esto es:", value=classification, height=100, key=f"classification_{frame_count}")
                frame_count += 1

        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")
            break

        if st.button("Parar", key="stop_button"):
            break
