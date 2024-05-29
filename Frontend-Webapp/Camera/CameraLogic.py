# En el archivo CameraLogic.py
import cv2
from streamlit_webrtc import VideoProcessorBase, VideoTransformerBase
import av

class CameraLogic:
    def __init__(self):
        pass
    
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
        self.last_processed_frame = None

    def recv(self, frame, original = False):
        img = frame.to_ndarray(format="bgr24")
        if original == True:
            processed_img = self.camera_processor.process_frame_og(img)
        else:
            processed_img = self.camera_processor.process_frame(img)
        # Almacenar el último frame procesado
        self.last_processed_frame = processed_img  
        return av.VideoFrame.from_ndarray(processed_img, format="bgr24")