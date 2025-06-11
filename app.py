import pandas as pd
import plotly.express as px
import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Análise de Carros Usados",
    page_icon="🚗",
    layout="wide"
)

# CSS PERSONALIZADO
st.markdown("""
<style>
    /* Fundo suave e temático */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Título com degrade violeta-aquamarine */
    h1 {
        background: linear-gradient(45deg, #6a3093, #7FFFD4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
    /* Botões com efeito hover */
    .stButton>button {
        background: linear-gradient(to right, #6a3093, #7FFFD4);
        color: white;
        border: none;
        transition: all 0.4s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    /* Abas estilizadas */
    .stTabs [aria-selected="true"] {
        color: #6a3093 !important;
        border-bottom: 3px solid #7FFFD4;
    }
</style>
""", unsafe_allow_html=True)

# CARREGAMENTO DOS DADOS
car_data = pd.read_csv('vehicles.csv')

# HEADER
st.markdown("# 🚗 Análise de Anúncios de Carros Usados")
st.markdown("Visualizações interativas com a paleta Viridis 🌈")

# SIDEBAR
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2063/2063512.png", width=80)
    st.title("Filtros")
    
    # Filtro por ano
    year_range = st.slider(
        "Selecione o intervalo de anos:",
        min_value=int(car_data['model_year'].min()),
        max_value=int(car_data['model_year'].max()),
        value=(2010, 2020)
    )
    
    # Filtro por preço
    price_range = st.slider(
        "Faixa de preço (USD):",
        min_value=int(car_data['price'].min()),
        max_value=int(car_data['price'].max()),
        value=(5000, 30000)
    )

# APLICAR FILTROS
filtered_data = car_data[
    (car_data['model_year'] >= year_range[0]) & 
    (car_data['model_year'] <= year_range[1]) &
    (car_data['price'] >= price_range[0]) & 
    (car_data['price'] <= price_range[1])
]

# ABAS
tab1, tab2, tab3 = st.tabs(["📊 Dados", "📈 Histograma", "✨ Dispersão"])

with tab1:
    st.subheader("Dados Filtrados")
    if st.button("Carregar dados", key="load_data"):
        st.dataframe(filtered_data.style.background_gradient(
            cmap='viridis', 
            subset=['price', 'odometer']
        ), height=500)
        st.metric("Total de veículos", len(filtered_data))

with tab2:
    st.subheader("Histograma de Quilometragem")
    if st.checkbox("Mostrar histograma", key="hist"):
        fig = px.histogram(
            filtered_data,
            x="odometer",
            nbins=30,
            color_discrete_sequence=['#440154'],  # Roxo mais escuro do Viridis
            labels={'odometer': 'Quilometragem'},
            template='plotly_white'
        )
        fig.update_layout(
            hoverlabel=dict(bgcolor="#404788")  # Roxo médio
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Gráfico de Dispersão")
    if st.checkbox("Mostrar dispersão", key="scatter"):
        fig = px.scatter(
            filtered_data,
            x="odometer",
            y="price",
            color="model_year",
            color_continuous_scale='viridis',  # ESCALA VIRIDIS OFICIAL
            hover_name="model",
            size="price",  # Tamanho dos pontos varia com o preço
            labels={
                'odometer': 'Quilometragem',
                'price': 'Preço (USD)',
                'model_year': 'Ano'
            }
        )
        fig.update_traces(
            marker=dict(opacity=0.8, line=dict(width=0.5, color='white'))
        )
        fig.update_layout(
            coloraxis_colorbar=dict(title="Ano", len=0.8)
        )
        st.plotly_chart(fig, use_container_width=True)

# RODAPÉ
st.markdown("---")
st.markdown("🎨 Paleta Viridis | ✨ by Adélia Cúrio 🐋")
