from pydantic import BaseModel
from typing import Set, Dict, List, Tuple

class Meudpda(BaseModel):
    """
    Modelo de entrada para um Autômato com Pilha Determinístico (DPDA).

    Esse modelo define a estrutura de um DPDA, incluindo seus estados, símbolos de entrada, símbolos da pilha, transições,
    estado inicial, símbolo inicial da pilha, estados finais e a entrada a ser processada.
    """

    states: Set[str]
    input_symbols: Set[str]
    stack_symbols: Set[str]
    transitions: Dict[str, Dict[str, Dict[str, list]]]
    initial_state: str
    initial_stack_symbol: str
    final_states: Set[str]
    input: str