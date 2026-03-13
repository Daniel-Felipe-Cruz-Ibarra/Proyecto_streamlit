import pandas as pd
import streamlit as st

#Carga de datos
url = 'https://github.com/Jorge-Hugo-Duarte-Guzman/practica-github/raw/refs/heads/main/data_sint_oper_pred_clas.csv'
df = pd.read_csv(url)


#Analisis y procesamiento

df_tipo_vuelo = df['TIPO_VUELO'].value_counts().reset_index()
estadisticos = df_tipo_vuelo['count'].describe()
maximo = estadisticos['max']
minimo = estadisticos['min']
media = estadisticos['mean']

#Visualización de datos

st.title('Datos de operaciones')

col1, col2, col3 = st. columns(3)

with col1:
    st.metric('Maximo', f'{maximo:.0f}', border=True)
with col2:
    st.metric('minimo', f'{minimo:.0f}', border=True)
with col3:
    st.metric('media', f'{media:.0f}', border=True)


st.dataframe(df)

st.subheader('Maximo')
st.text(maximo)
st.subheader('minimo')
st.text(minimo)
st.subheader('media')
st.text(media)

