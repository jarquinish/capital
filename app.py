import streamlit as st

# Configuración general
st.set_page_config(
    page_title="Calculadora CAPM",
    page_icon="📈",
    layout="centered"
)

# Estilos personalizados
st.markdown("""
    <style>
        .stApp {
            background-color: #f7f9fc;
        }

        section[data-testid="stSidebar"] {
            background-color: #d8f0ff;
        }

        .resultado-box {
            background-color: #000000;
            color: #ffffff;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-top: 25px;
        }

        .formula-box {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 10px;
            border-left: 5px solid #ff6a00;
            margin-top: 20px;
            font-size: 17px;
        }

        div.stButton > button {
            background-color: #ff6a00;
            color: white;
            border-radius: 10px;
            padding: 12px 24px;
            font-weight: bold;
            border: none;
            width: 100%;
        }

        div.stButton > button:hover {
            background-color: #e65c00;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("📈 Calculadora CAPM")
st.write("Calcula el rendimiento esperado de un activo usando el modelo **Capital Asset Pricing Model**.")

# Sidebar
st.sidebar.title("Parámetros del modelo")
st.sidebar.write("Ingresa los datos necesarios para calcular el rendimiento esperado.")

tasa_libre_riesgo = st.sidebar.number_input(
    "Tasa libre de riesgo (%)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)

beta = st.sidebar.number_input(
    "Beta del activo",
    min_value=0.0,
    max_value=5.0,
    value=1.0,
    step=0.1
)

rendimiento_mercado = st.sidebar.number_input(
    "Rendimiento esperado del mercado (%)",
    min_value=0.0,
    max_value=100.0,
    value=12.0,
    step=0.1
)

# Explicación
st.markdown("""
<div class="formula-box">
    <strong>Fórmula CAPM:</strong><br><br>
    Rendimiento esperado = Tasa libre de riesgo + Beta × 
    (Rendimiento del mercado - Tasa libre de riesgo)
</div>
""", unsafe_allow_html=True)

# Botón de cálculo
if st.button("Calcular CAPM"):
    capm = tasa_libre_riesgo + beta * (rendimiento_mercado - tasa_libre_riesgo)

    st.markdown(f"""
        <div class="resultado-box">
            Rendimiento esperado:<br>
            {capm:.2f}%
        </div>
    """, unsafe_allow_html=True)

    st.success("✅ Cálculo realizado correctamente.")

else:
    st.info("Ingresa los valores en el tablero lateral y presiona el botón para calcular.")
