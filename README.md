Trabalho de Teoria da Computação

Este projeto implementa autômatos finitos determinísticos (DFA), autômatos com pilha (DPDA) e máquinas de Turing (TM) utilizando FastAPI para expor uma API que permite testar e visualizar esses autômatos.

🚀 Configuração e Execução do Projeto

1️⃣ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

Python 3.9+

Pip

Virtualenv (opcional, mas recomendado)

2️⃣ Instalação

Clone o repositório e instale as dependências:
# Clone o repositório
git clone https://github.com/matheusmegale/trabalho-teoria-da-computacao.git
cd trabalho-teoria-da-computacao

# Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

3️⃣ Executando a API
uvicorn main:app --reload

A API estará disponível em http://127.0.0.1:8000 e a documentação interativa pode ser acessada em http://127.0.0.1:8000/docs.
