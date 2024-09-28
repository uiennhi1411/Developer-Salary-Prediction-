import streamlit as st
from streamlit_lottie import st_lottie
import json


@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
def show_intro_page():
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.title("Introduction to predict salary app")
            st.divider()
            st.markdown(
            """    
            ## Predict developer's salary 
            ### _Please select the function in sidebar menu_
            """
            )
        with col2:
            lottie2 = load_lottiefile("./app/static/intro.json")
            st_lottie(lottie2,key='intro',height=300,width=400)

    st.divider()

    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader('EXPLORE PAGE')
        st.write('Visualization')
    with col2:
        st.subheader('PREDICT PAGE')
        st.write('Predict Salary base on ML Model Page')
    with col3:
        st.subheader('ABOUT PAGE')
        st.write('Summary about my team and project')



        