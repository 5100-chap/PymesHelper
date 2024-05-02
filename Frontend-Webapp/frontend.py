import cv2
import numpy as np
import streamlit as st

# camara
cap = cv2.VideoCapture(0)

st.set_page_config(page_title="Camera Contour Test")
frame_placeholder = st.empty()
st.write("## Video con renderizacion de objetos")

while True:
    # lectura de frames
    ret, frame = cap.read()
    frame_blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    # parse frame to space color HSV
    hsv = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2HSV)

    # define color ranges
    lower_bound = np.array([0, 60, 0])
    upper_bound = np.array([179, 255, 255])

    # mask with only the colors in range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # find contours from binary mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # filter contours
    for countour in contours:
        if cv2.contourArea(countour)>600:
            cv2.drawContours(frame, [countour], -1, (0, 0, 255), 2)
    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels='RGB')
cap.release()