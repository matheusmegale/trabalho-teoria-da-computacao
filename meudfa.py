from pydantic import BaseModel, Field
from typing import Set, Dict


class Meudfa(BaseModel):
    """
    Modelo de entrada para um Autômato Finito Determinístico (DFA).

    Esse modelo define a estrutura de um DFA, incluindo seus estados, símbolos de entrada, transições,
    estado inicial, estados finais e a entrada a ser processada.
    """
    states: Set[str] = Field(..., description="Conjunto de estados do DFA.")
    input_symbols: Set[str] = Field(..., description="Conjunto de símbolos de entrada do DFA.")
    transitions: Dict[str, Dict[str, str]] = Field(
        ...,
        description=(
            "Dicionário de transições do DFA, onde a chave do primeiro nível representa o estado atual, "
            "e a chave do segundo nível representa o símbolo de entrada. O valor é o próximo estado."
        )
    )
    initial_state: str = Field(..., description="Estado inicial do DFA.")
    final_states: Set[str] = Field(..., description="Conjunto de estados finais do DFA.")
    input: str = Field(..., description="String de entrada a ser processada pelo DFA.")



