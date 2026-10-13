from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

ARQUIVO = "tarefa.json"
app = FastAPI()

def ler_arquivo_json():
    with open(ARQUIVO, 'r') as arquivo:
        dados = json.load(arquivo)
        return dados

def escrever_arquivo_json(dados):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

@app.get("/tarefas")
def listar_tarefas():
    tarefas = ler_arquivo_json()
    return tarefas

class Tarefa(BaseModel):
    tarefa: str
    status: str

@app.post("/tarefas/")
def adicionar_tarefa(tarefa: Tarefa):
    tarefas = ler_arquivo_json()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "tarefa": tarefa.tarefa,
        "status": tarefa.status,
        "pontos": random.randint(10, 50)
    }
    tarefas.append(nova_tarefa)
    escrever_arquivo_json(tarefas)
    return {"message": "Tarefa adicionada com sucesso", "tarefa": nova_tarefa} 

@app.put("/tarefas/{id_tarefa}")
def modificar_tarefa(id_tarefa: int, tarefa: Tarefa):
    tarefas = ler_arquivo_json()
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["tarefa"] = tarefa.tarefa
            t["status"] = tarefa.status
            escrever_arquivo_json(tarefas)
            return {"message": "Tarefa modificada com sucesso", "tarefa": t}
    return {"message": "Tarefa não encontrada"}

@app.delete("/tarefas/{id_tarefa}")
def deletar_tarefa(id_tarefa: int):
    tarefa = ler_arquivo_json()
    for t in tarefa:
        if t["id"] == id_tarefa:
            tarefa.remove(t)
            escrever_arquivo_json(tarefa)
            return {"message": "Tarefa deletada com sucesso"}
    return {"message": "Tarefa não encontrada"}


@app.get("/tarefas/roleta")
def roleta_tarefas():
    tarefas = ler_arquivo_json()
    if status := [tarefa for tarefa in tarefas if tarefa["status"] == "Pendente"]:
        tarefa_selecionada = random.choice(status)
        return {"message": "Tarefa selecionada", "tarefa": tarefa_selecionada}


@app.put("/tarefas/{id_tarefa}/concluir")
def concluir_tarefa(id_tarefa: int):
    tarefa = ler_arquivo_json()
    for t in tarefa:
        if t["id"] == id_tarefa:
            t["status"] = "Concluída"
            escrever_arquivo_json(tarefa)
            return {"message": "Tarefa concluída com sucesso", "tarefa": t}
    return {"message": "Tarefa não encontrada"}