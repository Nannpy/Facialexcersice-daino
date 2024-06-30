import streamlit as st
import cv2
import numpy as np

st.title("Webcam with Streamlit")

# สร้างฟังก์ชันสำหรับเปิดเว็บแคมและอ่านเฟรม
def capture_webcam():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# แสดงวิดีโอจากเว็บแคมแบบเรียลไทม์
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    FRAME_WINDOW.image(frame, channels="BGR")
cap.release()
