import cv2
import streamlit as st 
import numpy as np
import tempfile

cap = VideoCapture(1)

st.title('Facial Excersice with DaiNo Game')

frame_placeholder = st.empty()

stop_button = st.button('stop')

while cap.is0pened() and not stop_button:
    ret , frame = cap.read()

    if not ret:
        st.write('Game over')
        break

    frame = cv2.cvtColor(frame  ,cv2_COLOR.BGR2RGB)
    frame_placeholder.image(frame ,chanels='RGB')

    if cv2.waitkey(1) & 0xFF == ord('q') or stop_button:
        break

cap.release()
cv2.destroyAllWindows()
