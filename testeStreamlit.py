import streamlit as st
import pandas as pd
import numpy as np
import psycopg2

st.title('Pesquisadores do cesar is :orange[cool].')
st.subheader('Projeto desenvolvido para o PET-Facep com parceria com o CESAR School')
st.caption('Orientadores: Rafael Ferreira e Luana Cristina')
st.write('O projeto se trata de extrair dados de curriculos de pesquisadores da Plataforma Lattes ultilizado o lucyLattes para automatizar o processo (O lucyLattes é programado em python), os dados que precisamos extrair foram os seguintes:')
st.write('O projeto se trata de extrair dados de curriculos de pesquisadores da Plataforma Lattes ultilizado o lucyLattes para automatizar o processo (O lucyLattes é programado em python), os dados que precisamos extrair foram os seguintes:')

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])
conn = init_connection()

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()





#rows = run_query("SELECT ano from patentes")
#st.bar_chart(rows)

