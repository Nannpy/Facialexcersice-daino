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

    frame = cv2.cvtColor(frame  ,cv2.COLOR_BAYER_BG2BGR)
    frame_placeholder.image(frame ,chanels='RGB')

    if cv2.waitkey(1) & 0xFF == ord('q') or stop_button:
        break

cap.release()
cv2.destroyAllWindows()
