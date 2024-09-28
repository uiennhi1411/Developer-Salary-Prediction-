import joblib
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from config import config
import json



st.cache_data()
def load_model():
    return joblib.load(config.CKPT_PATH)

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

def convert_currency(amount, to_currency):
    rounded_amount = round(abs(amount) * config.CURRENCY_RATES[to_currency], 3)
    if to_currency == 'VND':
        return "{:,.3f}".format(rounded_amount) + ' ' + config.CURRENCY_SYMBOLS[to_currency]
    else:
        return config.CURRENCY_SYMBOLS[to_currency] + "{:,.3f}".format(rounded_amount)




def show_predict_page():
    model = load_model()
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.title("Calculating Salary Prediction")
            st.divider()
            # st.subheader("Predict salary base on developer's skill, position, experience")
            # st.subheader("*Predict salary base on developer's skill, position, experience*")
            st.markdown(
            """    
            ## Predict salary base on developer's skill, position, experience.
            ### _Select features below_
            """
            )
        with col2:
            lottie2 = load_lottiefile("./app/static/pred.json")
            st_lottie(lottie2,key='pred',height=300,width=400)

    st.divider()

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            # Country
            st.markdown("## Country")
            Country = st.selectbox("Select your country", config.COUNTRY, key=4)

            # DevType
            st.markdown("## Type of Developer")
            DevType = st.selectbox("Select your type of developer", config.DEV_TYPES, key=3)

        with col2:
            # EdLevel
            st.markdown("## Education Level")
            EdLevel = st.selectbox("Select your education level", config.ED_LEVEL, key=2)

            # Age
            st.markdown("## Age")
            Age = st.selectbox("Select your age", config.AGE, key=5)

    # RemoteWork
    st.markdown("## Work type")
    # RemoteWork = st.selectbox("On-site, Remote or Hybrid?", config.REMOTE_WORK, key=1)
    RemoteWork = st.radio('Select your work type', config.REMOTE_WORK, index=1,horizontal=True)

    # YearsCodePro
    st.markdown("## Years of experience")
    YearsCodePro = st.slider("Select your years of experience", min_value=0, max_value=46, step=1, value=10)
    if YearsCodePro == 0:
        YearsCodePro = 0.5
    YearsCodePro = float(YearsCodePro)

    st.markdown("## Show more features")

    with st.expander('Hide/unhide'):

        st.markdown('### You can select mutltiple options')

        # LanguageHaveWorkedWith
        st.markdown("## Programming Language")
        LanguageHaveWorkedWith = st.multiselect("Language you have worked with", config.LANGUAGE)

        languages = [0] * len(config.LANGUAGE)
        if LanguageHaveWorkedWith:
            for language in LanguageHaveWorkedWith:
                languages[config.LANGUAGE.index(language)] = 1.
        
        # DatabaseHaveWorkedWith
        st.markdown("## Database")
        DatabasesHaveWorkedWith = st.multiselect("Databases you have worked with", config.DATABASES)

        databases = [0] * len(config.DATABASES)
        if DatabasesHaveWorkedWith:
            for db in DatabasesHaveWorkedWith:
                databases[config.DATABASES.index(db)] = 1

        # PlatformHaveWorkedWith
        st.markdown("## Platform")
        PlatformHaveWorkedWith = st.multiselect("Cloud Platform you have worked with", config.PLATFORM)

        platforms = [0] * len(config.PLATFORM)
        if PlatformHaveWorkedWith:
            for platform in PlatformHaveWorkedWith:
                platforms[config.PLATFORM.index(platform)] = 1.

        # ToolsTechHaveWorkedWith
        st.markdown("## Tools Tech")
        ToolsTechHaveWorkedWith = st.multiselect("Tools tech you have worked with", config.TOOLS_TECH)

        tools_tech = [0] * len(config.TOOLS_TECH)
        if ToolsTechHaveWorkedWith:
            for tool in ToolsTechHaveWorkedWith:
                tools_tech[config.TOOLS_TECH.index(tool)] = 1.
        
        # CollabToolsTechHaveWorkedWith
        st.markdown("## Colab Tools")
        CollabToolHaveWorkedWith = st.multiselect("Colab tools you have worked with", config.COLLAB_TOOLS)

        collab_tools = [0] * len(config.COLLAB_TOOLS)
        if CollabToolHaveWorkedWith:
            for tool in CollabToolHaveWorkedWith:
                collab_tools[config.COLLAB_TOOLS.index(tool)] = 1


    INPUTS = [RemoteWork] + [EdLevel] + [YearsCodePro] + [DevType] + [Country] + [Age] + languages + databases + platforms + tools_tech + collab_tools 
    INPUTS = [INPUTS]
    input_df = pd.DataFrame(INPUTS, columns=config.COLUMNS)


    # predict_flag = st.button("Show Predict", type = 'primary')

    # if predict_flag:

    st.divider()
    l,r = st.columns(2)
    with l:
        st.title('Predict result')
        currency = st.selectbox("Choose currency you want to dislay",config.CURRENCY)
        pred = model.predict(input_df)
        salary_month = convert_currency(float(pred/12),currency)
        salary_year = convert_currency(float(pred),currency)

        if currency:
        
            st.subheader("Your salary's prediction")
            col1,col2 = st.columns(2)
            col1.metric("Per month",salary_month)
            col2.metric("Per year", salary_year)
    with r:
        lottie2 = load_lottiefile("./app/static/pred2.json")
        st_lottie(lottie2,key='pred2',height=300,width=400)
    # st.divider()
        

