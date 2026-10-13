import streamlit as st
import requests

st.title("Atendimento ao Cliente")

lista = requests.get("http://localhost:8000/atendimentos_clientes").json()

st.radio("Escolha uma opção:", ["Entrar na fila", "Listar atendimentos", "Chamar cliente", "Sortear brinde"], key="opcao")

match st.session_state.opcao:
    case "Entrar na fila":
        nome_cliente = st.text_input("Digite seu nome:")
        if st.button("Entrar na fila"):
            if nome_cliente:
                response = requests.post("http://localhost:8000/atendimentos_clientes", json={"nome": nome_cliente})
                if response.status_code == 200:
                    st.success(f"Você entrou na fila! Código do cupom: {response.json()['codigo_cupom']}")
                else:
                    st.error("Erro ao entrar na fila.")
            else:
                st.warning("Por favor, digite seu nome.")

    case "Sortear brinde":
        if st.button("Sortear brinde"):
            response = requests.get("http://localhost:8000/atendimentos/sorteio-brinde")
        
            if response.status_code == 200:
                st.balloons()
                st.success(f"Cliente sorteado para atendimento VIP: **{response.json()['nome_cliente']}**")
            else:
                st.error("Erro ao sortear brinde.")