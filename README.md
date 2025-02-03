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

📌 Exemplos de Uso da API

1️⃣ Testando um DFA

Requisição:

{
  "states": ["q0", "q1", "q2"],
  "input_symbols": ["0", "1"],
  "transitions": {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q0", "1": "q2"},
    "q2": {"0": "q2", "1": "q1"}
  },
  "initial_state": "q0",
  "final_states": ["q1"],
  "input": "00011111"
}

Resposta:

{
  "Will this input be accepted? ->": true,
  "diagram_path": "/static/dfa_diagram.png"
}

2️⃣ Testando um DPDA

Requisição:
```json
{
  "states": ["q0", "q1", "q2", "q3"],
  "input_symbols": ["a", "b"],
  "stack_symbols": ["0", "1"],
  "transitions": {
    "q0": {
      "a": { "0": ["q1", ["1", "0"]] }
    },
    "q1": {
      "a": { "1": ["q1", ["1", "1"]] },
      "b": { "1": ["q2", ""] }
    },
    "q2": {
      "b": { "1": ["q2", ""] },
      "": { "0": ["q3", ["0"]] }
    }
  },
  "initial_state": "q0",
  "initial_stack_symbol": "0",
  "final_states": ["q3"],
  "input": "aaaabbbb"
}
```

Resposta:

{
  "Will this input be accepted? ->": true,
  "diagram_path": "/static/dpda_diagram.png"
}
