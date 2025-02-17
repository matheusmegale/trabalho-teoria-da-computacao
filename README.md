<h1>Trabalho de Teoria da Computação</h1>

Este projeto implementa autômatos finitos determinísticos (DFA), autômatos com pilha (DPDA) e máquinas de Turing (TM) utilizando FastAPI para expor uma API que permite testar e visualizar esses autômatos. 

<h2>🚀 Configuração e Execução do Projeto</h2>

1️⃣ Instale as dependências

Certifique-se de que você tem o Python 3.8+ instalado. Execute:
```sh
pip install automata-lib
```

```sh
pip install 'automata-lib[visual]'
```

```sh
pip install "fastapi[standard]"
```

2️⃣ Inicie a API

```sh
fastapi dev main.py
```

A API estará disponível em http://127.0.0.1:8000 e a documentação interativa pode ser acessada em http://127.0.0.1:8000/docs.

Nota: a visualização dos autômatos só será possível em http://127.0.0.1:8000. 

<h2>📌 Exemplos de Uso da API</h2>

Nota: para todas as máquinas, a palavra de entrada a ser verificada é o último elemento do JSON

<h3>1️⃣ Testando um DFA</h3>

DFA que aceita palavras que terminam em um número ímpar de '1's

Requisição:
```json
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
```

Resposta:

![image](https://github.com/user-attachments/assets/2e0924f4-4336-4b1c-921a-c82e4f269d81)

As informações da máquina (estados, trasições, etc) serão exibidas acima dessa resposta.


<h3>2️⃣ Testando um DPDA</h3>

DPDA que combina zero ou mais 'a's, seguidos pelo mesmo número de 'b's

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

![image](https://github.com/user-attachments/assets/c0e3829d-a368-484d-9a04-9a4eea984672)

As informações da máquina (estados, trasições, etc) serão exibidas acima dessa resposta.


<h3>3️⃣ Testando uma Máquina de Turing</h3>

DTM que combina todas as cadeias que começam com '0's, seguidas pelo mesmo número de '1's

Requisição:
```json
{
    "states": ["q0", "q1", "q2", "q3", "q4"],
    "input_symbols": ["0", "1"],
    "tape_symbols": ["0", "1", "x", "y", "."],
    "transitions": {
        "q0": {
            "0": ["q1", "x", "R"],
            "y": ["q3", "y", "R"]
        },
        "q1": {
            "0": ["q1", "0", "R"],
            "1": ["q2", "y", "L"],
            "y": ["q1", "y", "R"]
        },
        "q2": {
            "0": ["q2", "0", "L"],
            "x": ["q0", "x", "R"],
            "y": ["q2", "y", "L"]
        },
        "q3": {
            "y": ["q3", "y", "R"],
            ".": ["q4", ".", "R"]
        }
    },
    "initial_state": "q0",
    "blank_symbol": ".",
    "final_states": ["q4"],
		"input": "000111"
}
```

Resposta:

![image](https://github.com/user-attachments/assets/dca6f842-6c66-4ee1-ad0e-f2c2fb093221)

As informações da máquina (estados, trasições, etc) serão exibidas acima dessa resposta.

⚠️ Nota: Máquinas de Turing não geram diagramas visuais.

<h2>⚠️ Limitações e Pressupostos</h2>

✅ O que funciona:

Implementação de DFA, DPDA e DTM

Geração de diagramas para DFA e DPDA

Validação de entrada na API via Pydantic

❌ Limitações:

A biblioteca Automata não suporta diagramas para Máquinas de Turing.
