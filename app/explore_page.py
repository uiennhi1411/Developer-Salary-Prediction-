import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from config import config
import seaborn as sns
import json


@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
    
@st.cache_data
def load_data():
    df = pd.read_csv(config.DATA_PATH)
    df = df.drop(["Unnamed: 0"],axis=1)
    return df

@st.cache_data
def plot_remotework(df):
    remotework = df["RemoteWork"].value_counts()
    remotework_df = remotework.to_frame()
    labels = remotework.index
    values = remotework.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=remotework_df)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_edlevel(df):
    edlevel = df["EdLevel"].value_counts()
    edlevel_df = edlevel.to_frame()
    labels = edlevel.index
    values = edlevel.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=edlevel_df)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)



@st.cache_data
def plot_yearscodepro(df):
    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="YearsCodePro", hue="EdLevel", kde=True, bins=30)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="YearsCodePro", hue="RemoteWork", kde=True, bins=30)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

@st.cache_data
def plot_devtype(df):
    type = df["DevType"].value_counts().head(10)  
    labels = type.index
    values = type.values

    col1, col2 = st.columns(2)
    
    with col1: 
        st.bar_chart(data=type)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_country(df):
    country = df["Country"].value_counts().head(10)
    labels = country.index
    values = country.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=country)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_age(df):
    age = df["Age"].value_counts()
    age_df = age.to_frame()
    labels = age.index
    values = age.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=age_df)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_programlang(df):
    lang = df[config.LANGUAGE]
    lang_sum = lang.sum().sort_values(ascending=False)
    lang_df = lang_sum.to_frame()

    labels = lang_sum.index
    values = lang_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=lang_df)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_platform(df): 
    platform = df[config.PLATFORM]
    platform_sum = platform.sum().sort_values(ascending=False)
    platform_df = platform_sum.to_frame()

    labels = platform_sum.index
    values = platform_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=platform_df)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_databases(df):
    databases = df[config.DATABASES]
    db_sum = databases.sum().sort_values(ascending=False)
    db_df = db_sum.to_frame()

    labels = db_sum.index
    values = db_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        st.bar_chart(data=db_df)  
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_tools_tech(df):
    tools_tech = df[config.TOOLS_TECH]
    tools_tech_sum = tools_tech.sum().sort_values(ascending=False)
    tools_tech_df = tools_tech_sum.to_frame()

    labels = tools_tech_sum.index
    values = tools_tech_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=tools_tech_df)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)

@st.cache_data
def plot_collab_tools(df):
    collab_tools = df[config.COLLAB_TOOLS]
    collab_tools_sum = collab_tools.sum().sort_values(ascending=False)
    collab_tools_df = collab_tools_sum.to_frame()

    labels = collab_tools_sum.index
    values = collab_tools_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        st.bar_chart(data=collab_tools_sum)
    with col2:
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%.0f%%')
        plt.setp(texts, color='black')  
        plt.setp(autotexts, color='black')  
        fig.patch.set_alpha(0)
        st.pyplot(fig)


@st.cache_data
def plot_salary(df):
    # fig = plt.figure(figsize=(9, 7))
    # ax = sns.boxplot(data=df, x="Country", y="Salary")
    # plt.xticks(rotation=90)
    # st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="EdLevel", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="Age", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="RemoteWork", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def show_explore_page():
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.title("Data Visualization")
            st.divider()
            # st.subheader("Predict salary base on developer's skill, position, experience")
            # st.subheader("*Predict salary base on developer's skill, position, experience*")
            st.markdown(
            """    
            ## Visualize Stack Overflow Annual Survey 2023 processed
            ### _Select features you want to visualize_
            """
            )
        with col2:
            lottie2 = load_lottiefile("./app/static/explore.json")
            st_lottie(lottie2,key='explore',height=300,width=400)

    df = load_data()

    show_df = st.radio('Show cleaned dataset ?', ['Yes','No'], index=1,horizontal=True)
    if show_df == 'Yes':
        st.dataframe(df)

    
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10, tab11, tab12 = st.tabs(config.FEATURE_LIST)

    with tab1:
        st.markdown("## Remote Work")
        plot_remotework(df)
    with tab2:
        st.markdown("## Education Level")
        plot_edlevel(df)
    with tab3:
        st.markdown("## Years of Experience")
        plot_yearscodepro(df)
    with tab4:
        st.markdown("## Developer Type")
        plot_devtype(df)
    with tab5:
        st.markdown("## Country")
        plot_country(df)
    with tab6:
        st.markdown("## Age ")
        plot_age(df)
    with tab7:
        st.markdown("## Programming Language ")
        plot_programlang(df)
    with tab8:
        st.markdown("## Databases")
        plot_databases(df)
    with tab9:
        st.markdown("## Cloud Platform")
        plot_platform(df)
    with tab10:
        st.markdown("## Tools & Technologies")
        plot_tools_tech(df)
    with tab11:
        st.markdown("## Collaboration Tools")
        plot_collab_tools(df)
    with tab12:
        st.markdown("## Salary Yearly")
        plot_salary(df)
