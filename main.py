# Link para o repositorio:
# https://github.com/matheusmegale/trabalho-teoria-da-computacao

import os
from fastapi import FastAPI
from mt import Mt
from automata.tm.dtm import DTM
from meudfa import Meudfa
from meudpda import Meudpda
from automata.fa.dfa import DFA
from automata.pda.dpda import DPDA
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Autômatos API", description="API para validação de autômatos", version="1.0")

# Diretório da pasta static
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Caminhos para as imagens
IMAGE_PATH_DFA = os.path.join(STATIC_DIR, "dfa_diagram.png")
IMAGE_PATH_DPDA = os.path.join(STATIC_DIR, "dpda_diagram.png")

# Montar a pasta static para servir arquivos estáticos
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=FileResponse, summary="Servir página inicial")
async def serve_home():
    """
    Retorna a página HTML inicial do projeto.
    """
    return os.path.join(STATIC_DIR, "index.html")


@app.get("/teste", summary="Teste de conexão")
def read_root():
    """
    Endpoint de teste para verificar se a API está funcionando corretamente.
    """
    return {"Trabalho de Teoria da Computação"}


@app.post("/dtm/", summary="Validar Máquina de Turing Determinística (DTM)")
def validate_dtm(turing: Mt):
    """
    Valida uma Máquina de Turing Determinística (DTM) com base na entrada fornecida.

    - **states**: Conjunto de estados
    - **input_symbols**: Símbolos de entrada
    - **tape_symbols**: Símbolos da fita
    - **transitions**: Funções de transição
    - **initial_state**: Estado inicial
    - **blank_symbol**: Símbolo branco
    - **final_states**: Estados finais
    - **input**: Entrada a ser processada
    """
    dtm = DTM(
        states=turing.states,
        input_symbols=turing.input_symbols,
        tape_symbols=turing.tape_symbols,
        transitions=turing.transitions,
        initial_state=turing.initial_state,
        blank_symbol=turing.blank_symbol,
        final_states=turing.final_states
    )

    return {
        "states": turing.states,
        "input_symbols": turing.input_symbols,
        "tape_symbols": turing.tape_symbols,
        "transitions": turing.transitions,
        "initial_state": turing.initial_state,
        "blank_symbol": turing.blank_symbol,
        "final_states": turing.final_states,
        "Will this input be accepted? ->": dtm.accepts_input(turing.input)
    }


@app.post("/dfa/", summary="Validar Autômato Finito Determinístico (DFA)")
def validate_dfa(dfa: Meudfa):
    """
    Valida um Autômato Finito Determinístico (DFA) e gera seu diagrama.

    - **states**: Conjunto de estados
    - **input_symbols**: Símbolos de entrada
    - **transitions**: Funções de transição
    - **initial_state**: Estado inicial
    - **final_states**: Estados finais
    - **input**: Entrada a ser processada
    """
    my_dfa = DFA(
        states=dfa.states,
        input_symbols=dfa.input_symbols,
        transitions=dfa.transitions,
        initial_state=dfa.initial_state,
        final_states=dfa.final_states
    )

    diagram = my_dfa.show_diagram(path="static/dfa_diagram.png")
    diagram.draw(IMAGE_PATH_DFA, format="png")

    return {
        "states": dfa.states,
        "input_symbols": dfa.input_symbols,
        "transitions": dfa.transitions,
        "initial_state": dfa.initial_state,
        "final_states": dfa.final_states,
        "Will this input be accepted? ->": my_dfa.accepts_input(dfa.input),
        "diagram_path": "/static/dfa_diagram.png"
    }


@app.post("/dpda/", summary="Validar Autômato com Pilha Determinístico (DPDA)")
def validate_dpda(dpda: Meudpda):
    """
    Valida um Autômato com Pilha Determinístico (DPDA) e gera seu diagrama.

    - **states**: Conjunto de estados
    - **input_symbols**: Símbolos de entrada
    - **stack_symbols**: Símbolos da pilha
    - **transitions**: Funções de transição
    - **initial_state**: Estado inicial
    - **initial_stack_symbol**: Símbolo inicial da pilha
    - **final_states**: Estados finais
    - **input**: Entrada a ser processada
    """
    my_dpda = DPDA(
        states=dpda.states,
        input_symbols=dpda.input_symbols,
        stack_symbols=dpda.stack_symbols,
        transitions=dpda.transitions,
        initial_state=dpda.initial_state,
        initial_stack_symbol=dpda.initial_stack_symbol,
        final_states=dpda.final_states,
    )

    diagram = my_dpda.show_diagram(path="static/dpda_diagram.png")
    diagram.draw(IMAGE_PATH_DPDA, format="png")

    return {
        "states": dpda.states,
        "input_symbols": dpda.input_symbols,
        "stack_symbols": dpda.stack_symbols,
        "transitions": dpda.transitions,
        "initial_state": dpda.initial_state,
        "initial_stack_symbol": dpda.initial_stack_symbol,
        "final_states": dpda.final_states,
        "Will this input be accepted? ->": my_dpda.accepts_input(dpda.input),
        "diagram_path": "/static/dpda_diagram.png"
    }
