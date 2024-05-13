import pandas as pd
import plotly.express as px
import streamlit as st  

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construcción dispersión')

if scatter_button:
    st.write('Crea el gráfico de dispersión')
    figu = px.scatter(car_data, x='model', y='model_year')
    st.plotly_chart(figu, use_container_width=True)
