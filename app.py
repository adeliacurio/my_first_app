import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('~/vehicles.csv') # lendo os dados
st.header('Vendas de carros a partir de anúncios') # título do aplicativo
st.write('Este aplicativo cria um histograma para o conjunto de dados de anúncios de vendas de carros') # descrição do aplicativo
st.write('O conjunto de dados contém informações sobre anúncios de vendas de carros, incluindo o odômetro, preço e outros detalhes.') # descrição do conjunto de dados
st.write('O histograma será criado com base no odômetro dos carros.') # descrição do histograma
st.write('O gráfico de dispersão será criado com base no odômetro e no preço dos carros, colorido pelo ano do carro.') # descrição do gráfico de dispersão
# criar um botão para carregar os dados
load_button = st.button('Carregar dados') # criar um botão
if load_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Carregando os dados do conjunto de dados de anúncios de vendas de carros')
    # exibir os dados
    st.dataframe(car_data) # exibir os dados em um dataframe interativo
# criar um botão para gerar o histograma
hist_check = st.checkbox('Criar histograma') # criar uma caixa de seleção

if hist_check: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar um botão para gerar o gráfico de dispersão
scatter_check = st.checkbox('Criar gráfico de dispersão') # criar uma caixa de seleção
if scatter_check: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price", color="year")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)