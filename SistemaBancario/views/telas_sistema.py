from datetime import date


layout_tela_principal = [
    { "lin":  1, "col": 1, "value" : "╔═══════════════════════════════════════════════════════════════════════════╦══════════════════════╗" },
    { "lin":  2, "col": 1, "value" : "║                                                                           ║ Data:                ║" },
    { "lin":  3, "col": 1, "value" : "╠═══════════════════════════════════════════════════════════════════════════╩══════════════════════╣" },
    { "lin":  4, "col": 1, "value" : "║      ┌─────────────┐  ┌─────────────┐  ┌───┐     ┌───┐                                           ║" },
    { "lin":  5, "col": 1, "value" : "║     █│             │ █│             │ █│   │\   █│   │                                           ║" },
    { "lin":  6, "col": 1, "value" : "║     █│   ┌─────────┘ █└────┐   ┌────┘ █│     \  █│   │                                           ║" },
    { "lin":  7, "col": 1, "value" : "║     █│   │▀▀▀▀▀▀▀▀   ▀▀▀▀▀█│   │      █│      \ █│   │                                           ║" },
    { "lin":  8, "col": 1, "value" : "║     █│   └──────┐         █│   │      █│       \▀│   │                                           ║" },
    { "lin":  9, "col": 1, "value" : "║     █│          │         █│   │      █│   │\   \│   │                                           ║" },
    { "lin": 10, "col": 1, "value" : "║     █│   ┌──────┘         █│   │      █│   │ \       │                                           ║" },
    { "lin": 11, "col": 1, "value" : "║     █│   │▀▀▀▀▀           █│   │      █│   │  \      │                                           ║" },
    { "lin": 12, "col": 1, "value" : "║     █│   │           ▄┌────┘   └────┐ █│   │   \     │                                           ║" },
    { "lin": 13, "col": 1, "value" : "║     █│   │           █│             │ █│   │    \│   │                                           ║" },
    { "lin": 14, "col": 1, "value" : "║     █└───┘           █└─────────────┘ █└───┘    █└───┘                                           ║" },
    { "lin": 15, "col": 1, "value" : "║     ▀▀▀▀▀            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀     ▀▀▀▀▀                                            ║" },
    { "lin": 16, "col": 1, "value" : "║                               ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───┐     ┌───┐ ║" },
    { "lin": 17, "col": 1, "value" : "║                              █│             │ █│             │ █│             │ █│   │    █│   │ ║" },
    { "lin": 18, "col": 1, "value" : "║                              █└────┐   ┌────┘ █│   ┌─────────┘ █│   ┌─────────┘ █│   │    █│   │ ║" },
    { "lin": 19, "col": 1, "value" : "║                              ▀▀▀▀▀█│   │      █│   │▀▀▀▀▀▀▀▀▀  █│   │▀▀▀▀▀▀▀▀▀  █│   │    █│   │ ║" },
    { "lin": 20, "col": 1, "value" : "║                                   █│   │      █│   └──────┐    █│   │           █│   └─────┘   │ ║" },
    { "lin": 21, "col": 1, "value" : "║                                   █│   │      █│          │    █│   │           █│             │ ║" },
    { "lin": 22, "col": 1, "value" : "║                                   █│   │      █│   ┌──────┘    █│   │           █│   ┌─────┐   │ ║" },
    { "lin": 23, "col": 1, "value" : "║                                   █│   │      █│   │▀▀▀▀▀▀     █│   │           █│   │▀▀▀▀█│   │ ║" },
    { "lin": 24, "col": 1, "value" : "║                                   █│   │      █│   └─────────┐ █│   └─────────┐ █│   │    █│   │ ║" },
    { "lin": 25, "col": 1, "value" : "║                                   █│   │      █│             │ █│             │ █│   │    █│   │ ║" },
    { "lin": 26, "col": 1, "value" : "║                                   █└───┘      █└─────────────┘ █└─────────────┘ █└───┘    █└───┘ ║" },
    { "lin": 27, "col": 1, "value" : "║                                   ▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀     ▀▀▀▀▀  ║" },
    { "lin": 28, "col": 1, "value" : f"║                                                             DIO - By André Rogério Bononi © {date.today().year} ║" },
    { "lin": 29, "col": 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin": 30, "col": 1, "value" : "║                                                                                                  ║" },
    { "lin": 31, "col": 1, "value" : "╚══════════════════════════════════════════════════════════════════════════════════════════════════╝" }
]

titulos_telas = {
    "menu_principal" : "FINTECHDIO - MENU PRINCIPAL - SISTEMA BANCARIO".center(75, " "),
    "cadastro_correntista" : "CADASTRO DE CORRENTISTAS".center(98, " "),
    "relatorio_correntista" : "RELAÇÃO DOS CORRENTISTAS CADASTRADOS".center(75, " "),
    "cadastro_contacorrente" : "CADASTRO DE CONTA CORRENTE".center(75, " "),
    "relatorio_contacorrente" : "RELAÇÃO DE CONTAS CADASTRADAS".center(75, " "),
    "lancamento_transacao" : "LANÇAMENTO DE TRANSAÇÕES".center(98, " "),
    "relatorio_transacao" : "RELAÇÃO DAS TRANSAÇÕES REGISTRADAS".center(75, " ")
}

layout_correntistas = [
    { "lin":  5, "col":  1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col":  1, "value" : "║ CPF ...: [              ]                                            Data Cadastro: [          ] ║" },
    { "lin":  9, "col":  1, "value" : "║ Nome ..: [                                                 ] Data Nasc: [          ] Idade [   ] ║" },
    { "lin": 11, "col":  1, "value" : "║ Ender..: [                                                               ] Número : [          ] ║" },
    { "lin": 13, "col":  1, "value" : "║ Compl..: [                           ] Bairro: [                                               ] ║" },
    { "lin": 15, "col":  1, "value" : "║ Cidade : [                                                          ] UF: [  ] CEP: [          ] ║" },
    { "lin": 17, "col":  1, "value" : "║ Fone ..: [             ]                        Status: (   ) ATIVO (   ) RESTRITO (   ) INATIVO ║" },
    { "lin": 30, "col":  2, "value" : "(N)OVA      (A)LTERAR      (E)XCLUIR      (C)ONSULTAR      (L)ISTAR      (R)ETORNAR".center(98, " ") }
]

layout_rel_correntistas = [
    { "lin":  3, "col" : 1, "value" : "╠════════════════╦════════════════════════════════════════════════════╦═════╩═════════╦════════════╣" },
    { "lin":  4, "col" : 1, "value" : "║ Número do CPF  ║ Nome do Correntista                                ║ Telefone      ║ Dt. Nascto ║" },
    { "lin":  5, "col" : 1, "value" : "╠════════════════╬════════════════════════════════════════════════════╬═══════════════╬════════════╣" },
    { "lin":  6, "col" : 1, "value" : "║                ║                                                    ║               ║            ║" },
    { "lin": 29, "col" : 1, "value" : "╠════════════════╩════════════════════════════════════════════════════╩═══════════════╩════════════╣" },
    { "lin": 30, "col" : 1, "value" : "║ (P)RÓXIMA PÁGINA                                                                      (R)ETORNAR ║" }
]

layout_contacorrente = [
    { "lin":  5, "col": 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col": 1, "value" : "║ Conta N°: [          ]                                            Data de Abertura: [          ] ║" },
    { "lin":  9, "col": 1, "value" : "║ CPF ....: [              ][                                        ] Cliente Desde: [          ] ║" },
    { "lin": 11, "col": 1, "value" : "║ ┌────────────────────┐ ┌────────────────────────────┐                                            ║" },
    { "lin": 12, "col": 1, "value" : "║ │   Tipo de Conta    │ │      Situação da Conta     │                                            ║" },
    { "lin": 13, "col": 1, "value" : "║ ├────────────────────┤ ├────────────────────────────┤                                            ║" },
    { "lin": 14, "col": 1, "value" : "║ │ ( ) Poupanca       │ │ ( ) Pendente               │                                            ║" },
    { "lin": 15, "col": 1, "value" : "║ │ ( ) Conta Corrente │ │ ( ) Ativa                  │                                            ║" },
    { "lin": 16, "col": 1, "value" : "║ │                    │ │ ( ) Bloqueada              │                                            ║" },
    { "lin": 17, "col": 1, "value" : "║ │  Limite Especial:  │ │ ( ) Inativa                │                                            ║" },
    { "lin": 18, "col": 1, "value" : "║ │  R$ [            ] │ │ ( ) Encerrada [          ] │                                            ║" },
    { "lin": 19, "col": 1, "value" : "║ └────────────────────┘ └────────────────────────────┘                                            ║" },
    { "lin": 30, "col": 2, "value" : "(N)OVA      (A)LTERAR      (E)XCLUIR      (C)ONSULTAR      (L)ISTAR      (R)ETORNAR".center(98, " ") }
]

layout_rel_contas = [
    { "lin":  3, "col" : 1, "value" : "╠════════════╦════════════════╦════════════════╦════════════════════════════╩═════════╦════════════╣" },
    { "lin":  4, "col" : 1, "value" : "║  Nº CONTA  ║ TIPO DE CONTA  ║  CPF  CLIENTE  ║ NOME DO CLIENTE                      ║  ABERTURA  ║" },
    { "lin":  5, "col" : 1, "value" : "╠════════════╬════════════════╬════════════════╬══════════════════════════════════════╬════════════╣" },
    { "lin":  6, "col" : 1, "value" : "║            ║                ║                ║                                      ║            ║" },
    { "lin": 29, "col" : 1, "value" : "╠════════════╩════════════════╩════════════════╩══════════════════════════════════════╩════════════╣" },
    { "lin": 30, "col" : 1, "value" : "║ (P)RÓXIMA PÁGINA                                                                      (R)ETORNAR ║" }
]

layout_transacoes = [
    { "lin":  5, "col" : 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col" : 1, "value" : "║  Transação Nº: [          ]                      ┌──────────────────────────┐                    ║" },
    { "lin":  8, "col" : 1, "value" : "║                                                  │ Data: [               ]  │                    ║" },
    { "lin":  9, "col" : 1, "value" : "║  Conta Nº ...: [          ]                      ├──────────────────────────┤                    ║" },
    { "lin": 10, "col" : 1, "value" : "║  [                                         ]     │      Tipo Transação      │                    ║" },
    { "lin": 11, "col" : 1, "value" : "║                                                  ├──────────────────────────┤                    ║" },
    { "lin": 12, "col" : 1, "value" : "║  Saldo Atual : [              ]                  │ ( ) Depósito   ( ) Saque │                    ║" },
    { "lin": 13, "col" : 1, "value" : "║                                                  │                          │                    ║" },
    { "lin": 14, "col" : 1, "value" : "║  Saldo Final : [              ]                  │ Valor : [              ] │                    ║" },
    { "lin": 15, "col" : 1, "value" : "║                                                  └──────────────────────────┘                    ║" },
    { "lin": 30, "col" : 1, "value" : "(N)OVA      (A)LTERAR      (E)XCLUIR      (C)ONSULTAR      (L)ISTAR      (R)ETORNAR".center(98, " ") }
]

layout_rel_transacoes = [
    { "lin":  3, "col": 1, "value" : "╠══════════════════╦════════════╦════════════╦═════════════════╦════════════╩═══╦══════════════════╣" },
    { "lin":  4, "col": 1, "value" : "║ DATA/HORA        ║ CONTA Nº   ║ TIPO MOVTO ║ SALDO  ANTERIOR ║  VALOR  MOVTO  ║   SALDO  ATUAL   ║" },
    { "lin":  5, "col": 1, "value" : "╠══════════════════╬════════════╬════════════╬═════════════════╬════════════════╬══════════════════╣" },
    { "lin":  6, "col": 1, "value" : "║                  ║            ║            ║                 ║                ║                  ║" },
    { "lin": 29, "col": 1, "value" : "╠══════════════════╩════════════╩════════════╩═════════════════╩════════════════╩══════════════════╣" },
    { "lin": 30, "col": 1, "value" : "║ (P)ROXIMA PÁGINA                                                                      (R)ETORNAR ║" }
]