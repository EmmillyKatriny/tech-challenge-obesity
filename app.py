import streamlit as st
import joblib
import pandas as pd

# =========================
# Configuração da Página
# =========================

st.set_page_config(page_title="Predição de Obesidade", layout="centered")

model = joblib.load("modelo_obesidade.pkl")

st.title("Predição de Nível de Obesidade")
st.markdown("Preencha as informações abaixo para estimar o nível de obesidade com base no modelo treinado.")

st.divider()

# =========================
# Dados Básicos
# =========================

st.subheader("Dados Corporais")

age = st.number_input("Idade", min_value=0, max_value=100, step=1)
height = st.number_input("Altura (em metros)", min_value=0.0, max_value=2.5, step=0.01)
weight = st.number_input("Peso (em kg)", min_value=0.0, max_value=300.0, step=0.1)

st.divider()

# =========================
# Hábitos Alimentares
# =========================

st.subheader("Hábitos Alimentares")

fcvc = st.selectbox(
    "Com que frequência você consome vegetais?",
    [1, 2, 3],
    format_func=lambda x: {
        1: "1 - Baixo consumo (raramente)",
        2: "2 - Consumo moderado",
        3: "3 - Consumo frequente"
    }[x]
)

ncp = st.selectbox(
    "Quantas refeições principais você faz por dia?",
    [1, 2, 3, 4]
)

favc = st.selectbox(
    "Consome alimentos altamente calóricos com frequência?",
    ["yes", "no"],
    format_func=lambda x: "Sim" if x == "yes" else "Não"
)

caec = st.selectbox(
    "Costuma comer entre as refeições?",
    ["no", "Sometimes", "Frequently", "Always"],
    format_func=lambda x: {
        "no": "Não",
        "Sometimes": "Às vezes",
        "Frequently": "Frequentemente",
        "Always": "Sempre"
    }[x]
)

calc = st.selectbox(
    "Consumo de álcool",
    ["no", "Sometimes", "Frequently", "Always"],
    format_func=lambda x: {
        "no": "Não consome",
        "Sometimes": "Ocasionalmente",
        "Frequently": "Frequentemente",
        "Always": "Sempre"
    }[x]
)

st.divider()

# =========================
# Estilo de Vida
# =========================

st.subheader("Estilo de Vida")

ch2o = st.selectbox(
    "Consumo diário de água",
    [1, 2, 3],
    format_func=lambda x: {
        1: "1 - Baixo",
        2: "2 - Moderado",
        3: "3 - Alto"
    }[x]
)

faf = st.selectbox(
    "Nível de atividade física semanal",
    [0, 1, 2, 3],
    format_func=lambda x: {
        0: "0 - Nenhuma",
        1: "1 - Baixa (1–2x por semana)",
        2: "2 - Moderada (3–4x por semana)",
        3: "3 - Alta (5x ou mais por semana)"
    }[x]
)

tue = st.selectbox(
    "Tempo diário em frente a telas (TV, celular, computador)",
    [0, 1, 2],
    format_func=lambda x: {
        0: "0 - Baixo",
        1: "1 - Moderado",
        2: "2 - Alto"
    }[x]
)

mtrans = st.selectbox(
    "Principal meio de transporte",
    ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"],
    format_func=lambda x: {
        "Public_Transportation": "Transporte público",
        "Walking": "Caminhada",
        "Automobile": "Carro",
        "Motorbike": "Moto",
        "Bike": "Bicicleta"
    }[x]
)

st.divider()

# =========================
# Informações Pessoais
# =========================

st.subheader(" Informações Pessoais")

gender = st.selectbox(
    "Gênero",
    ["Female", "Male"],
    format_func=lambda x: "Feminino" if x == "Female" else "Masculino"
)

family_history = st.selectbox(
    "Histórico familiar de obesidade?",
    ["yes", "no"],
    format_func=lambda x: "Sim" if x == "yes" else "Não"
)

smoke = st.selectbox(
    "Fuma?",
    ["yes", "no"],
    format_func=lambda x: "Sim" if x == "yes" else "Não"
)

scc = st.selectbox(
    "Monitora consumo calórico?",
    ["yes", "no"],
    format_func=lambda x: "Sim" if x == "yes" else "Não"
)

st.divider()

# =========================
# Botão de Previsão
# =========================

if st.button("Prever Nível de Obesidade"):
    
    if height == 0:
        st.error("Altura não pode ser zero.")
    else:
        bmi = weight / (height ** 2)

        input_data = pd.DataFrame({
            "Gender": [gender],
            "Age": [age],
            "Height": [height],
            "Weight": [weight],
            "family_history": [family_history],
            "FAVC": [favc],
            "FCVC": [fcvc],
            "NCP": [ncp],
            "CAEC": [caec],
            "SMOKE": [smoke],
            "CH2O": [ch2o],
            "SCC": [scc],
            "FAF": [faf],
            "TUE": [tue],
            "CALC": [calc],
            "MTRANS": [mtrans],
            "BMI": [bmi]
        })

        prediction = model.predict(input_data)

        st.subheader("Resultado")

        st.info(f"Seu IMC calculado é: **{bmi:.2f}**")

        st.success(f"Nível previsto pelo modelo: **{prediction[0]}**")