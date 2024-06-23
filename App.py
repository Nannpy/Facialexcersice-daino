import streamlit as st
import troch

# model_path = 'Model.py'

# model = torch.load('Model.py')
# model.eval() 

st.title("T-Rex Runner Game")

game_url = "https://vianroyal.github.io/t-rex-runner/"
st.markdown(
    f"""
    <iframe src="{game_url}" width="800" height="600" frameborder="0"></iframe>
    """,
    unsafe_allow_html=True
)
