import streamlit as st
import pandas as pd
import json
import sqlite3
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

#import plotly.express as px

# import shap
#import matplotlib.pyplot as plt

@st.cache
def get_data(filename):
    taxi_data= pd.read_csv(filename)
    return taxi_data


# Création d'une base de données Sqlite3 en mémoire
# cnx = sqlite3.connect(':memory:')
# Création d'une base de données Sqlite3 en mémoire
cnx = sqlite3.connect('steam_games.db')
curs = cnx.cursor()
# Interoger la table df avec une requête SQL
sql = "select * from steam_games"
curs.execute(sql)
#print(curs.fetchone())
df=pd.read_sql(sql, cnx)
#print(df.head())

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

st.markdown(
    '''
    <style>
    .main { 
    background-color: #F5F5F5; 
    }
    </style>
    ''',
    unsafe_allow_html=True
    )

with header:
    st.title("Welcome to my Deployment **Steam-Analytics**!")
    image = Image.open('steam.jpg')
    st.image(image, width=200)
    st.write('---')

with dataset:
    st.header('Steam dataset')
    st.text('This is our Database:')
    st.write(df.head(5))

    #st.subheader('Pickup pulocation_dist')
    #pulocation_dist= pd.DataFrame(df['PULocationID'].value_counts()).head(50)
    #st.bar_chart(pulocation_dist)

with features:
    st.header('Steam features')
    st.text('This is description....')
    st.markdown('* **first feature:** I create this feature because...')
    st.markdown('* **second feature:** I create this feature because...')

with model_training:
    st.header('Training model')
    st.text('This is description....')
    sel_col, disp_col = st.columns(2)
    #first column:
    max_depth = sel_col.slider('what should be the depth of the model ?',min_value=10,max_value=100,value=20,step=10)
    n_estimator = sel_col.selectbox('How many trees should there be ?',options=[100,200,300,'no limit'],index=0)

    st.text('Here is the list of feature to select:')
    #st.write(taxi_data.columns)

    input_feature = sel_col.text_input('Which feature should be use as the input:','PULocationID')

    # 2nd column:
    # Plot Closing Price of Query Symbol
    def price_plot(df):
        fig = plt.figure()
        sns.lmplot(x='total_positive', y='final', data=df)
        return st.pyplot(fig)


    disp_col.subheader('Prepare for plotting..')
    fig, ax = plt.subplots()
    #sns.lmplot(x='total_positive', y='final', data=df)
    sns.distplot(df['final'])
    #plt.bar(df['total_positive'],df['final'])
    #plt.hist(df['total_positive'], bins=5, rwidth=0.8)
    plt.xlabel("final")
    plt.ylabel("Frequency")
    plt.xlim(0,500)
    plt.ylim(0,0.01)
    #sns.lmplot(x='review_score', y='total_positive', data=df)
    #plt.title("review total vs.positive score")
    #plt.xlabel("x=review_score")
    #plt.ylabel("y=total_positive")
    #plt.xlim(0,100)
    #plt.ylim(0,0.001)
    disp_col.write(fig)

    disp_col.subheader('Output 01..')
    #disp_col.write( Var_Output_01)
