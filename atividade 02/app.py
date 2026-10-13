import streamlit as st
import requests

st.title("ROLETA DE TAREFAS & PRODUTIVIDADE")

lista_item = requests.get("http://localhost:8000/tarefas").json()
st.table(lista_item)

st.selectbox("Selecione uma tarefa", options=[f"{item['id']}: {item['tarefa']}: {item['pontos']}: {item['status']}" for item in lista_item], key="id_tarefa") 

st.radio("Deseja modificar ou deletar", options=["Adicionar", "Modificar", "Deletar"], key="opcao")

match st.session_state.opcao:
    case "Adicionar":
        with st.form("Adicionar Tarefa"):
            tarefa = st.text_input("Tarefa", placeholder = "Digite a tarefa")
            status = st.selectbox("Status", ["Pendente", "Concluída"])
            if st.form_submit_button("Adicionar"):
                response = requests.post("http://localhost:8000/tarefas", json={"tarefa": tarefa, "status": status})
                if response.status_code == 200:
                    st.success("Tarefa adicionada com sucesso!")    
                else:
                    st.error("Erro ao adicionar tarefa.")
    case "Modificar":
        with st.form("Modificar Tarefa"):
            tarefa = st.text_input("Nova tarefa", placeholder = "Digite a nova tarefa")
            status = st.selectbox("Status", ["Pendente", "Concluída"])
            if st.form_submit_button("Modificar"):
                id_tarefa = int(st.session_state.id_tarefa.split(":")[0])
                response = requests.put(f"http://localhost:8000/tarefas/{id_tarefa}", json={"tarefa": tarefa, "status": status})
                if response.status_code == 200:
                    st.success("Tarefa modificada com sucesso!")    
                else:
                    st.error("Erro ao modificar tarefa.")
    case "Deletar":
        with st.form("Deletar Tarefa"):
            if st.form_submit_button("Deletar"):
                id_tarefa = int(st.session_state.id_tarefa.split(":")[0])
                response = requests.delete(f"http://localhost:8000/tarefas/{id_tarefa}")
                if response.status_code == 200:
                    st.success("Tarefa deletada com sucesso!")    
                else:
                    st.error("Erro ao deletar tarefa.")



if st.button("Sortear Tarefa"):
    response = requests.get("http://localhost:8000/tarefas/roleta").json()
    t = response.get("tarefa")
    st.success(f"Tarefa sorteada: {t['tarefa']} - Status: {t['status']} - Pontos: {t['pontos']}")   

if st.button("Concluir Tarefa"):
    id_tarefa = int(st.session_state.id_tarefa.split(":")[0])
    response = requests.put(f"http://localhost:8000/tarefas/{id_tarefa}/concluir")
    if response.status_code == 200:
        st.success("Tarefa concluída com sucesso!")    
    else:
        st.error("Erro ao concluir tarefa.")