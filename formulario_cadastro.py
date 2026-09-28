import streamlit as st


st.title("Formulário de cadastro")

with st.form("formulario_cadastro"):
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    if email != "":
        if "@" not in email or "." not in email:
            st.error("Email inválido. Por favor, insira um email válido.")
        else:
            st.success("Email válido!")
    senha = st.text_input("Senha:", type="password")
    confirmar_senha = st.text_input("Confirmar senha:", type="password")
    if senha != confirmar_senha:
        st.error("As senhas não coincidem. Por favor, tente novamente.")
    data_nascimento = st.date_input("Data de nascimento:")
    genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])
    termos = st.checkbox("Aceito os termos e condições")
    submit_button = st.form_submit_button("Cadastrar")
