# Aplicações de exemplo com Streamlit

Este repositório reúne três aplicações pequenas e independentes, feitas em Python com Streamlit. Elas demonstram entradas, botões, conversões e validações simples em uma interface web.

## O que há no projeto

- `app.py`: calcula o Índice de Massa Corporal (IMC) a partir do peso e da altura.
- `conversor_unidades.py`: converte moedas, temperaturas e distâncias.
- `formulario_cadastro.py`: demonstra um formulário com dados pessoais, validações básicas de e-mail e senha e aceite dos termos.

Cada arquivo pode ser iniciado separadamente. O formulário é apenas uma demonstração: os dados não são enviados nem gravados em um banco de dados. A conversão de moedas consulta a API da [AwesomeAPI](https://economia.awesomeapi.com.br/), por isso precisa de acesso à internet.

## Requisitos

- Python 3.10 ou superior. O conversor usa `match/case`, sintaxe disponível a partir do Python 3.10.
- `pip`, que acompanha as instalações comuns do Python.
- Os pacotes `streamlit` e `requests`.
- Um navegador web. O Streamlit inicia um servidor local e mostra o endereço para abrir no navegador.
- Acesso à internet para instalar os pacotes e, no conversor, consultar cotações de moedas.

No macOS, a documentação do Streamlit também lista as ferramentas de linha de comando do Xcode como pré-requisito para a instalação. Consulte a [documentação oficial de instalação](https://docs.streamlit.io/get-started/installation/command-line) para detalhes.

## Instalação no Linux e macOS

Abra um terminal na pasta do projeto e crie um ambiente virtual:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install streamlit requests
```

No macOS, se as ferramentas de linha de comando do Xcode ainda não estiverem instaladas, execute:

```bash
xcode-select --install
```

Em algumas distribuições Linux, pode ser necessário instalar o suporte a `venv` usando o gerenciador de pacotes da distribuição.

## Instalação no Windows

Abra o PowerShell na pasta do projeto. O comando `py` é instalado pelo instalador oficial do Python:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install streamlit requests
```

Se estiver usando o Prompt de Comando (cmd.exe), ative o ambiente com:

```bat
.venv\Scripts\activate.bat
```

Depois da instalação, use os comandos abaixo no terminal com o ambiente virtual ativo.

## Executar uma aplicação

Na pasta do projeto, escolha **um** dos comandos:

```bash
streamlit run app.py
```

```bash
streamlit run conversor_unidades.py
```

```bash
streamlit run formulario_cadastro.py
```

O terminal informa o endereço local da aplicação. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

Se o comando `streamlit` não for encontrado, use a forma equivalente com o Python:

```bash
python -m streamlit run app.py
```

Substitua `app.py` pelo arquivo que deseja executar.
