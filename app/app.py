import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from intro_page import show_intro_page
from about_page import show_about_page
from explore_page import show_explore_page
from predict_page import show_predict_page



#Layout
st.set_page_config(
    page_title="Salary Predict App",
    layout="wide",
    page_icon=":mag_right:",
    initial_sidebar_state="expanded"
)

#Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

with st.sidebar:
    selected = option_menu('Menu', ["Intro", 'Explore','Predict','About'], 
        icons=['play-btn','graph-up','search', 'info-circle'],menu_icon='intersect', default_index=0)
    lottie = load_lottiefile("./app/static/sidebar.json")
    st_lottie(lottie,key='sidebar')


if selected == "Intro":
    show_intro_page()
elif selected == 'Explore':
    show_explore_page()
elif selected == 'Predict':
    show_predict_page()
else:
    show_about_page()

