import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Evaluación de vehículos de concesionaria')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button2 = st.button('Histograma vehículo vs condición')

if hist_button2:
    st.write('Compara el año del vehículo con su condición')
    fig = px.histogram(car_data, x='model_year', color='condition' )
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Diagrama de dispersion de precio por tipo de vehículo ')
if scatter_button:
    st.write('Compara el precio por tipo de vehículo ')
    fig = px.scatter(car_data, x='type', y='price')
    st.plotly_chart(fig, use_container_width=True)