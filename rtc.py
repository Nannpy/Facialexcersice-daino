# import streamlit as st  
# from streamlit_webrtc import webrtc_streamer
# import cv2
# import av 

# st.title('Daino Game camera Test')

# # webrtc_streamer(key = 'sample')

# class VideoProcessor :
#     def recv(self,frame):
#         img = frame.to_ndarray(format = 'bgr24')

#         img = cv2.cvtColor(cv2.Canny(img,100,200), cv2.COLOR_GRAY2BGR)

#         return av.VideoFrame.from_ndarray(img, format="bgr24")
    
# webrtc_streamer(key = 'edge', video_processor_factory = VideoProcessor)

import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

st.title("Webcam Streamlit App")
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
