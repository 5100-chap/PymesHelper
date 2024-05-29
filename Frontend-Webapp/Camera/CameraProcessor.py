import cv2
import numpy as np
import base64
import requests

class CameraProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def send_video(self, frame, ext='png'):
        try:
            _, video_data = cv2.imencode(f".{ext}", frame)
            video_bytes = base64.b64encode(video_data)

            if self.api_url:
                url = self.api_url + "/classify_video"
                response = requests.post(url, data=video_bytes)
                classification = response.json()["classification"]
            else:
                classification = "API URL no definida"

            return classification
        except Exception as e:
            return str(e)

    def process_frame(self, frame):
        frame_blurred = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2HSV)

        lower_bound = np.array([0, 60, 0])
        upper_bound = np.array([179, 255, 255])

        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 300:
                perimeter = cv2.arcLength(contour, True)
                circularity = (4 * np.pi * cv2.contourArea(contour) / (perimeter**2))

                if circularity <= 2.5:
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])

                    if cY < frame.shape[1] / 2:
                        cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)

        return frame
    
    def process_frame_og(self, frame):
        return frame