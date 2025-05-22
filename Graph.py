import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Manipulation de données et création de graphiques")

url = "https://github.com/mwaskom/seaborn-data.git"
data = pd.read_html(url)
liste = data[0]['Name'][5:28].to_list()
liste.append('')
liste.sort()



selected = st.selectbox('Quel DataSet souhaites-tu utiliser ? :', liste)

if selected != '':
    link = f"https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/{selected}"
    df = pd.read_csv(link)
    st.dataframe(df)
    
    col = df.columns.to_list()
    col.append('')
    col.sort()
    x = st.selectbox('Choisissez la série pour X :', col)
    y = st.selectbox('Choisissez la série pour Y :', col)
    
    graph_chart = ['','scatter_chart','bar_chart','line_chart']
    graph_options = st.selectbox('Quel graphique souhaites-tu utiliser ? :', graph_chart)
    
    if graph_options != '' and x !='' and y !='' and graph_options == graph_chart[1]:
        st.scatter_chart(df,x = x, y = y)
        aff = st.checkbox("Afficher la matrice de corrélation", value=False)
        if aff == True:
            st.write('Ma matrice de corrélation')
            fig, ax = plt.subplots()
            sns.heatmap(
                    df.corr(numeric_only = True),
                    annot = True,
                    center = 0,
                    vmin = -1,
                    vmax = 1,
                    cmap = sns.diverging_palette(350, 280, s=100, as_cmap = True)
                    )
            st.pyplot(fig)
        
    if graph_options != '' and x !='' and y !='' and graph_options == graph_chart[2]:
        st.bar_chart(df,x = x, y = y)
        aff = st.toggle("Afficher la matrice de corrélation (pour changer du st.checkbox)", value=False)
        if aff == True:
            st.write('Ma matrice de corrélation')
            fig, ax = plt.subplots()
            sns.heatmap(
                    df.corr(numeric_only = True),
                    annot = True,
                    center = 0,
                    vmin = -1,
                    vmax = 1,
                    cmap = sns.diverging_palette(350, 280, s=100, as_cmap = True)
                    )
            st.pyplot(fig)
 
        
    if graph_options != '' and x !='' and y !='' and graph_options == graph_chart[3]:
        st.line_chart(df,x = x, y = y)
        aff = st.toggle("Afficher la matrice de corrélation (je préfère st.toggle)", value=False)
        if aff == True:
            st.write('Ma matrice de corrélation')
            fig, ax = plt.subplots()
            sns.heatmap(
                    df.corr(numeric_only = True),
                    annot = True,
                    center = 0,
                    vmin = -1,
                    vmax = 1,
                    cmap = sns.diverging_palette(350, 280, s=100, as_cmap = True)
                    )
            st.pyplot(fig)
 

  
        