import cv2
import streamlit as st 
import numpy as np
import tempfile

cap = cv2.VideoCapture(0)

st.title('Facial Excersice with DaiNo Game')

frame_placeholder = st.empty()

stop_button = st.button('stop')

while cap.isOpened() and not stop_button:
    ret , frame = cap.read()

    if not ret:
        st.write('Game over')
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame ,channels='RGB')

    if cv2.waitKey(1) & 0xFF == ord('q') or stop_button:
        break

cap.release()
