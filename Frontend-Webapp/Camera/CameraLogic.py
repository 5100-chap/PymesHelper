import cv2
from streamlit_webrtc import VideoTransformerBase
class CameraLogic:
    def __init__(self):
        pass
    
    #Cambiar a logica de webrtc
    def list_cameras(self):
        available_cameras = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available_cameras.append(i)
                cap.release()
        return available_cameras

class VideoTransformer(VideoTransformerBase):
    def __init__(self, camera_processor):
        self.camera_processor = camera_processor

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Procesar el frame aquí
        classification = self.camera_processor.send_video(img)
        processed_frame = self.camera_processor.process_frame(img)

        return cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)