import streamlit as st
import pandas as pd
import json
#import plotly.express as px

# import shap
#import matplotlib.pyplot as plt

@st.cache
def get_data(filename):
    taxi_data= pd.read_csv(filename)
    return taxi_data

#open json
with open ('C:/Users/acer.LAPTOP-OODPR6CI/Documents/GitHub/Deployment/deployment-Steam-analytics/steam scrape/database.json') as f:
    data=json.load(f)

#example : df_1= get_data(data/taxi_data.csv)
df_1=pd.DataFrame(data)
pd.set_option('display.max_columns',111)
df=df_1.T


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
    st.write('---')

with dataset:
    st.header('Steam dataset')
    st.text('This is description....')
    #st.write(df.head(5))

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
    disp_col.subheader('Prepare for plotting..')
    disp_col.subheader('Output 01..')
    #disp_col.write( Var_Output_01)
    disp_col.subheader('Output 02..')
    #disp_col.write(Var_Output_02)
    disp_col.subheader('Output 03..')
    # disp_col.write(Var_Output_03)
