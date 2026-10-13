from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

ARQUIVO = "atendimentos.json"
app = FastAPI()

class cliente(BaseModel):
    nome: str

def ler_arquivo():
    try: 
        with open(ARQUIVO, "r")  as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def escrever_arquivo(dados):
    try:
        with open(ARQUIVO, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

@app.get("/atendimentos_clientes")
def listar_clientes():
    atendimentos = ler_arquivo()
    return atendimentos

@app.post("/atendimentos_clientes")
def entrar_na_fila(cliente: cliente):
    fila = ler_arquivo()
    novo = {
        "id": len(fila) + 1,
        "nome_cliente": cliente.nome,
        "codigo_cupom": f"CUPOM-{random.randint(1000, 9999)}",
        "desconto": random.choice([10, 15, 20, 25, 50]),
        "status": "Aguardando",
    }
    fila.append(novo)
    escrever_arquivo(fila)
    return novo

@app.put("/atendimentos/chamar/{id")
def chamar_client(id: int):
    chamar = ler_arquivo()
    for atendimento in chamar:
        if atendimento["id"] == id:
            atendimento["status"] = "Atendido"
            escrever_arquivo(chamar)
            return atendimento
    return {"message": "Cliente não encontrado."}


@app.get("/atendimentos/sorteio-brinde")
def sortear_brinde():
    atendimentos = ler_arquivo()
    aguardando = [atendimento for atendimento in atendimentos if atendimento["status"] == "Aguardando"]
    if not aguardando:
        return {"message": "Nenhum cliente aguardando para sorteio."}
    atendimento = random.choice(aguardando)
    atendimento["status"] = "Atendimento VIP"
    escrever_arquivo(atendimentos)
    return atendimento