from datetime import date
from models.tiposenum import PRETO_NO_BRANCO, RESET

layout_tela_principal = [
    { "lin":  1, "col": 1, "value" : "╔═══════════════════════════════════════════════════════════════════════════╦══════════════════════╗" },
    { "lin":  2, "col": 1, "value" : "║                                                                           ║ Data:                ║" },
    { "lin":  3, "col": 1, "value" : "╠═══════════════════════════════════════════════════════════════════════════╩══════════════════════╣" },
    { "lin":  4, "col": 1, "value" : "║                                                                                                  ║" },
    { "lin":  5, "col": 1, "value" : "║     ┌─────────────┐ ┌─────────────┐ ┌───┐     ┌───┐                                              ║" },
    { "lin":  6, "col": 1, "value" : "║     │             │ │             │ │   │\    │   │                                              ║" },
    { "lin":  7, "col": 1, "value" : "║     │   ┌─────────┘ └────┐   ┌────┘ │     \   │   │                                              ║" },
    { "lin":  8, "col": 1, "value" : "║     │   │                │   │      │      \  │   │                                              ║" },
    { "lin":  9, "col": 1, "value" : "║     │   └──────┐         │   │      │       \ │   │                                              ║" },
    { "lin": 10, "col": 1, "value" : "║     │          │         │   │      │   │\   \│   │                                              ║" },
    { "lin": 11, "col": 1, "value" : "║     │   ┌──────┘         │   │      │   │ \       │                                              ║" },
    { "lin": 12, "col": 1, "value" : "║     │   │                │   │      │   │  \      │                                              ║" },
    { "lin": 13, "col": 1, "value" : "║     │   │           ┌────┘   └────┐ │   │   \     │                                              ║" },
    { "lin": 14, "col": 1, "value" : "║     │   │           │             │ │   │    \│   │                                              ║" },
    { "lin": 15, "col": 1, "value" : "║     └───┘           └─────────────┘ └───┘     └───┘                                              ║" },
    { "lin": 16, "col": 1, "value" : "║                                                                                                  ║" },
    { "lin": 17, "col": 1, "value" : "║                                ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───┐     ┌───┐   ║" },
    { "lin": 18, "col": 1, "value" : "║                                │             │ │             │ │             │ │   │     │   │   ║" },
    { "lin": 19, "col": 1, "value" : "║                                └────┐   ┌────┘ │   ┌─────────┘ │   ┌─────────┘ │   │     │   │   ║" },
    { "lin": 20, "col": 1, "value" : "║                                     │   │      │   │           │   │           │   │     │   │   ║" },
    { "lin": 21, "col": 1, "value" : "║                                     │   │      │   └──────┐    │   │           │   └─────┘   │   ║" },
    { "lin": 22, "col": 1, "value" : "║                                     │   │      │          │    │   │           │             │   ║" },
    { "lin": 23, "col": 1, "value" : "║                                     │   │      │   ┌──────┘    │   │           │   ┌─────┐   │   ║" },
    { "lin": 24, "col": 1, "value" : "║                                     │   │      │   │           │   │           │   │     │   │   ║" },
    { "lin": 25, "col": 1, "value" : "║                                     │   │      │   └─────────┐ │   └─────────┐ │   │     │   │   ║" },
    { "lin": 26, "col": 1, "value" : "║                                     │   │      │             │ │             │ │   │     │   │   ║" },
    { "lin": 27, "col": 1, "value" : "║                                     └───┘      └─────────────┘ └─────────────┘ └───┘     └───┘   ║" },
    { "lin": 28, "col": 1, "value" : f"║                                                             DIO - By André Rogério Bononi © {date.today().year} ║" },
    { "lin": 29, "col": 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin": 30, "col": 1, "value" : "║                                                                                                  ║" },
    { "lin": 31, "col": 1, "value" : "╚══════════════════════════════════════════════════════════════════════════════════════════════════╝" }
]

titulos_telas = {
    "menu_principal" : "FINTECHDIO - MENU PRINCIPAL - SISTEMA BANCARIO".center(75, " "),
    "cadastro_correntista" : "CADASTRO DE CORRENTISTAS".center(75, " ")
}

layout_correntistas = [
    { "lin":  5, "col":  1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col":  1, "value" : "║ CPF ...: [              ]                                            Data Cadastro: [          ] ║" },
    { "lin":  8, "col":  1, "value" : "║ Nome ..: [                                                 ] Data Nasc: [          ] Idade [   ] ║" },
    { "lin":  9, "col":  1, "value" : "║ Ender..: [                                                               ] Número : [          ] ║" },
    { "lin": 10, "col":  1, "value" : "║ Compl..: [                           ] Bairro: [                                               ] ║" },
    { "lin": 11, "col":  1, "value" : "║ Cidade : [                                                          ] UF: [  ] CEP: [          ] ║" },
    { "lin": 12, "col":  1, "value" : "║ Fone ..: [             ]                        Status: (   ) ATIVO (   ) RESTRITO (   ) INATIVO ║" },
    { "lin": 30, "col":  2, "value" : "(N)ovo      (A)lterar      (E)xcluir      (C)onsultar      (L)istar      (R)etornar".center(98, " ") }
    # { "lin":  7, "col": 13, "value" : f"{PRETO_NO_BRANCO}{" ".center(14, " ")}{RESET}" },
    # { "lin":  7, "col": 88, "value" : f"{PRETO_NO_BRANCO}{" ".center(10, " ")}{RESET}" },
    # { "lin":  8, "col": 13, "value" : f"{PRETO_NO_BRANCO}{" ".center(49, " ")}{RESET}" },
    # { "lin":  8, "col": 76, "value" : f"{PRETO_NO_BRANCO}{" ".center(10, " ")}{RESET}" },
    # { "lin":  8, "col": 95, "value" : f"{PRETO_NO_BRANCO}{"   "}{RESET}" },
    # { "lin":  9, "col": 13, "value" : f"{PRETO_NO_BRANCO}{" ".center(76, " ")}{RESET}" },
    # { "lin":  9, "col": 88, "value" : f"{PRETO_NO_BRANCO}{" ".center(10, " ")}{RESET}" },
    # { "lin": 10, "col": 13, "value" : f"{PRETO_NO_BRANCO}{" ".center(27, " ")}{RESET}" },
    # { "lin": 10, "col": 51, "value" : f"{PRETO_NO_BRANCO}{" ".center(47, " ")}{RESET}" },
    # { "lin": 11, "col": 13, "value" : f"{PRETO_NO_BRANCO}{" ".center(58, " ")}{RESET}" },
    # { "lin": 11, "col": 78, "value" : f"{PRETO_NO_BRANCO}{"  "}{RESET}" },
    # { "lin": 11, "col": 88, "value" : f"{PRETO_NO_BRANCO}{" ".center(10, " ")}{RESET}" },
    # { "lin": 12, "col": 13, "value" : f"{PRETO_NO_BRANCO}{" ".center(13, " ")}{RESET}" },
    # { "lin": 12, "col": 61, "value" : f"{PRETO_NO_BRANCO}" "{RESET}" },
    # { "lin": 12, "col": 73, "value" : f"{PRETO_NO_BRANCO}" "{RESET}" },
    # { "lin": 12, "col": 88, "value" : f"{PRETO_NO_BRANCO}" "{RESET}" }
]