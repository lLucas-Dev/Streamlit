import streamlit as st


st.title("Calculadora de IMC")
st.write("Este app calcula o IMC baseado no peso e altura")
peso = st.number_input("Digite seu peso (KG):", value=70.0, step=0.1)
altura = st.number_input("Digite sua altura (M):", value=1.70, step=0.01)
imc = peso / (altura ** 2)

if st.button("Calcular IMC"):
    st.metric("Seu IMC é:", f"{imc:.2f}")
