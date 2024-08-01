import streamlit as st

game_url = 'http://staging.flappybird.io/'

# 'https://vianroyal.github.io/t-rex-runner/'
# 'http://wayou.github.io/t-rex-runner/'

with st.container():
    st.markdown(f"""
    <iframe src="{game_url}" width="100%" height="300" frameborder="0"></iframe>
    """, unsafe_allow_html=True)

# with st.container():
#     webcam_video = st.camera_input('')
