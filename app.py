import pandas as pd
import plotly.express as px
import streamlit as st

# configuração
st.set_page_config(
    page_title="Análise de Carros Usados",
    page_icon="🚗",
    layout="wide"
)

# css personalizado
st.markdown("""
<style>
    /* Tema roxo e aquamarine */
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
    }
    .stCheckbox>label {
        font-weight: bold;
        color: #6a3093 !important;
    }
</style>
""", unsafe_allow_html=True)

# carregando os dados
@st.cache_data  # Cache para melhor performance
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

# header
st.markdown("# 🚗 Análise de Carros Usados")
st.markdown("Visualizações interativas com histogramas e dispersões")

# gráficos obrigatórios
tab1, tab2, tab3 = st.tabs(["📊 Dados", "📈 Histogramas", "✨ Dispersões"])

with tab1:
    st.subheader("Amostra dos Dados")
    st.dataframe(
        car_data.sample(1000),  # Amostra aleatória
        height=500,
        hide_index=True,
        column_config={
            "price": st.column_config.NumberColumn("Preço (USD)", format="$%d"),
            "odometer": st.column_config.NumberColumn("Quilometragem", format="%d km")
        }
    )

with tab2:
    st.subheader("Distribuição de Valores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Histograma de Preços")
        fig = px.histogram(
            car_data,
            x="price",
            nbins=50,
            color_discrete_sequence=["#6a3093"],
            labels={"price": "Preço (USD)"}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Histograma de Quilometragem")
        fig = px.histogram(
            car_data,
            x="odometer",
            nbins=50,
            color_discrete_sequence=["#7FFFD4"],
            labels={"odometer": "Quilometragem"}
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Relação entre Variáveis")
    
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year",
        color_continuous_scale='viridis',
        hover_name="model",
        labels={
            "odometer": "Quilometragem",
            "price": "Preço (USD)",
            "model_year": "Ano do Modelo"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

# gráficos extras
st.markdown("---")
st.subheader("📌 Análises Complementares")

expander = st.expander("Ver mais visualizações")
with expander:
    tab4, tab5 = st.tabs(["📊 Por Tipo de Veículo", "🔥 Top Modelos"])
    
    with tab4:
        st.markdown("### Preço Médio por Tipo")
        avg_price = car_data.groupby('type')['price'].mean().sort_values()
        fig = px.bar(
            avg_price,
            color_discrete_sequence=["#9B59B6"],
            labels={"value": "Preço Médio (USD)", "type": "Tipo de Veículo"}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.markdown("### Modelos Mais Anunciados")
        top_models = car_data['model'].value_counts().head(10)
        fig = px.pie(
            top_models,
            names=top_models.index,
            color_discrete_sequence=px.colors.sequential.Viridis
        )
        st.plotly_chart(fig, use_container_width=True)

# rodapé
st.markdown("---")
st.markdown("✨ **Made by Adélia Cúrio** | **With IA 🐋**")
