import pandas as pd
import plotly.express as px
import streamlit as st

# ============== CONFIGURAÇÃO ==============
st.set_page_config(
    page_title="Análise de Carros Usados",
    page_icon="🚗",
    layout="wide"
)

# ============== CSS PERSONALIZADO ==============
st.markdown("""
<style>
    .stApp {
        background-color: #faf5ff;
    }
    h1 {
        color: #6a3093;
        border-bottom: 2px solid #7FFFD4;
        padding-bottom: 10px;
    }
    .stButton>button {
        background: linear-gradient(to right, #6a3093, #7FFFD4);
        color: white !important;
        margin-bottom: 10px;
    }
    .stCheckbox>label {
        font-weight: bold;
        color: #6a3093 !important;
    }
    div[data-testid="stExpander"] div[role="button"] p {
        font-size: 1.2rem;
        color: #6a3093 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============== CARREGAMENTO DOS DADOS ==============
@st.cache_data
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

# ============== HEADER ==============
st.markdown("# 🚗 Análise de Carros Usados")
st.markdown("Visualizações interativas com histogramas e dispersões")

# ============== BOTÃO PARA CARREGAR DADOS ==============
load_button = st.button('📤 Carregar Dados Completos')
if load_button:
    st.write("🔍 Carregando todos os dados...")
    st.dataframe(
        car_data,
        height=400,
        hide_index=True,
        column_config={
            "price": st.column_config.NumberColumn("Preço (USD)", format="$%d"),
            "odometer": st.column_config.NumberColumn("Quilometragem", format="%d km")
        }
    )
    st.metric("Total de veículos", len(car_data))

# ============== GRÁFICOS PRINCIPAIS ==============
st.markdown("---")
st.subheader("📊 Visualizações Principais")

# Histogramas
hist_check = st.checkbox('📈 Mostrar Histogramas')
if hist_check:
    st.write("Distribuição de valores nos dados:")
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(
            car_data,
            x="price",
            nbins=50,
            color_discrete_sequence=["#6a3093"],
            title="Distribuição de Preços"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.histogram(
            car_data,
            x="odometer",
            nbins=50,
            color_discrete_sequence=["#7FFFD4"],
            title="Distribuição de Quilometragem"
        )
        st.plotly_chart(fig, use_container_width=True)

# Dispersão
scatter_check = st.checkbox('✨ Mostrar Gráfico de Dispersão')
if scatter_check:
    st.write("Relação entre preço e quilometragem:")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year",
        color_continuous_scale='viridis',
        hover_name="model",
        labels={"price": "Preço (USD)", "odometer": "Quilometragem"}
    )
    st.plotly_chart(fig, use_container_width=True)

# ============== ANÁLISES COMPLEMENTARES ==============
st.markdown("---")
st.subheader("🧩 Análises Complementares")

# Checkbox para análises extras
show_extras = st.checkbox('🌟 Mostrar Análises Adicionais')
if show_extras:
    # Preço médio por tipo
    st.markdown("### Preço Médio por Tipo de Veículo")
    if st.checkbox('📊 Exibir gráfico'):
        avg_price = car_data.groupby('type')['price'].mean().sort_values()
        fig = px.bar(
            avg_price,
            color_discrete_sequence=["#9B59B6"],
            labels={"value": "Preço Médio (USD)"}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Top modelos
    st.markdown("### Modelos Mais Anunciados")
    if st.checkbox('🏆 Exibir top 10'):
        top_models = car_data['model'].value_counts().head(10)
        fig = px.pie(
            top_models,
            names=top_models.index,
            color_discrete_sequence=px.colors.sequential.Viridis,
            hole=0.3
        )
        st.plotly_chart(fig, use_container_width=True)

# ============== RODAPÉ ==============
st.markdown("---")
st.markdown("✨ **Made by Adélia Cúrio** | **With IA 🐋**")
