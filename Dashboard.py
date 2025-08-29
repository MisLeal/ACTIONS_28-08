import pandas as pd
import streamlit as st
import plotly.express as px



dados = pd.read_csv('dados_analisados.csv')
dados_crm = pd.read_csv('crm.csv')
st.title('ACTIONS TELEVENDAS :chart_with_upwards_trend:')
st.set_page_config(layout= 'wide')



def color_total(val):
    media = dados['Total'].mean()
    if val > media:
        return 'background-color: green; color: white'
    elif val < media:
        return 'background-color: yellow; color: black'
    else:
        return ''

 




coluna1, coluna2 = st.columns(2)

with coluna1:
    st.header("ACTIONS :pushpin:")
    st.dataframe(
    dados.style.applymap(color_total, subset=['Total'])
)
    
with coluna2:
    st.header('CRM :briefcase:')
    st.dataframe(
    dados_crm.style.applymap(color_total, subset=['Qtd_Historicos'])
)