from pydantic import BaseModel, Field
from typing import Set, Dict, Tuple

class Mt(BaseModel):
    """
    Modelo de entrada para uma Máquina de Turing Determinística (DTM).

    Esse modelo define a estrutura de uma Máquina de Turing, incluindo seus estados, símbolos de entrada,
    símbolos da fita, transições, estado inicial, símbolo branco, estados finais e a entrada a ser processada.
    """
    states: Set[str] = Field(..., description="Conjunto de estados da Máquina de Turing.")
    input_symbols: Set[str] = Field(..., description="Conjunto de símbolos de entrada.")
    tape_symbols: Set[str] = Field(..., description="Conjunto de símbolos da fita.")
    transitions: Dict[str, Dict[str, Tuple[str, str, str]]] = Field(
        ...,
        description=(
            "Dicionário de transições da Máquina de Turing, onde a chave do primeiro nível representa o estado atual, "
            "e a chave do segundo nível representa o símbolo lido na fita. O valor é uma tupla contendo "
            "(próximo estado, símbolo a ser escrito, direção do cabeçote ['L' para esquerda, 'R' para direita, 'S' para parado])."
        )
    )
    initial_state: str = Field(..., description="Estado inicial da Máquina de Turing.")
    blank_symbol: str = Field(..., description="Símbolo branco da fita.")
    final_states: Set[str] = Field(..., description="Conjunto de estados finais.")
    input: str = Field(..., description="String de entrada a ser processada pela Máquina de Turing.")
