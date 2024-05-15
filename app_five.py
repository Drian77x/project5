import pandas as pd
import plotly.express as px
import streamlit as st  

car_data = pd.read_csv('vehicles_us.csv')

st.header('AUTOS EN VENTA')

hist_button = st.button('Histograma de cantidad de autos por su año')

if hist_button:
    st.write('Autos en venta según año de fabricación')
    fig = px.histogram(car_data, 
                     x='model_year', 
                    labels={"model_year": "Año del auto"}, 
                    color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construcción dispersión')

if scatter_button:
    st.write('Dispersión de costo según el año')
    fig_two = px.scatter(car_data, 
                        x='model_year', 
                        y='price',
                        color_discrete_sequence=["red"], 
                        opacity=0.4,
                        labels={"model_year": "Año del modelo", 'price':'Precio de Venta'})
    st.plotly_chart(fig_two, use_container_width=True)


