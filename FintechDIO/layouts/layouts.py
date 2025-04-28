opcoes_disponiveis = {
    "menu_principal" : "[1 - CLIENTES]      [2 - CONTAS]      [3 - TRANSAÇÕES]      [4 - CONSULTAS]      [9 - SAIR]".center(98, " "),
    "cadastro_clientes" : "[C]ONSULTAR        [I]NCLUIR        [A]LTERAR        [E]XCLUIR        [L]ISTAR        [R]ETORNAR".center(98, " "),
    "cadastro_contas" : "[C]ONSULTAR        [I]NCLUIR        [A]LTERAR        [E]XCLUIR        [L]ISTAR        [R]ETORNAR".center(98, " "),
    "menu_transacoes" : "Escolha a opção desejada",
    "menu_consultas" : "Escolha a opção desejada",
    "opcoes_consultas" : "[P]RÓXIMA PÁGINA                           [N]OVA  CONSULTA                           [R]ETORNAR".center(98, " "),
    "consulta_saldo" : "Digite 0 (zero) no número da conta para encerrar"
}

titulo_telas = {
    "menu_principal" : "FINTECHDIO - SISTEMA FINANCEIRO - MENU PRINCIPAL".center(75, " "),
    "cadastro_clientes" : "CADASTRO DE CLIENTES".center(98, " "),
    "cadastro_contas" : "CADASTRO DE CONTAS".center(98, " "),
    "menu_transacoes" : "MENU TRANSAÇÕES".center(98, " "),
    "menu_consultas" : "MENU DE CONSULTAS".center(98, " "),
    "consulta_cliente" : "CONSULTA DE CLIENTES".center(75, " "),
    "consulta_conta" : "CONSULTA DE CONTAS".center(98, " "),
    "consulta_saldo" : "CONSULTA SALDO".center(98, " "),
    "consulta_extratos" : "CONSULTA EXTRATOS".center(75, " ")
}

operacoes_disponiveis = {
    "menu_principal" : [ 1, 2, 3, 4, 9 ],
    "cadastro_clientes" : [ "C", "I", "A","E", "L", "R" ],
    "cadastro_contas" : [ "C", "I", "A","E", "L", "R" ],
    "menu_transacoes" : [ 1, 2, 3, 4, 5, 6, 9 ],
    "menu_consultas" : [ 1, 2, 3, 4, 9 ],
    "opcoes_consultas" : [ "P", "N", "R" ]
}

layout_menu_principal = [
    { "lin":  1, "col" : 1, "value" : "╔═══════════════════════════════════════════════════════════════════════════╦══════════════════════╗" },
    { "lin":  2, "col" : 1, "value" : "║                                                                           ║ Data:                ║" },
    { "lin":  3, "col" : 1, "value" : "╠═══════════════════════════════════════════════════════════════════════════╩══════════════════════╣" },
    { "lin":  4, "col" : 1, "value" : "║   ┌───────────────┐    ┌───────────────┐   ┌───┐       ┌───┐                                     ║" },
    { "lin":  5, "col" : 1, "value" : "║  █│               │   █│               │  █│    ¯\    █│   │                                     ║" },
    { "lin":  6, "col" : 1, "value" : "║  █│   ┌───────────┘   █└─────┐   ┌─────┘  █│      \   █│   │                                     ║" },
    { "lin":  7, "col" : 1, "value" : "║  █│   │▀▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀█│   │        █│       \  █│   │                                     ║" },
    { "lin":  8, "col" : 1, "value" : "║  █│   └────────┐            █│   │        █│   │\   \ █│   │                                     ║" },
    { "lin":  9, "col" : 1, "value" : "║  █│            │            █│   │        █│   │▀\   \▀│   │                                     ║" },
    { "lin": 10, "col" : 1, "value" : "║  █│   ┌────────┘            █│   │        █│   │ █\   \│   │                                     ║" },
    { "lin": 11, "col" : 1, "value" : "║  █│   │▀▀▀▀▀▀▀▀             █│   │        █│   │  █\       │                                     ║" },
    { "lin": 12, "col" : 1, "value" : "║  █│   │                ┌─────┘   └─────┐  █│   │   █\      │                                     ║" },
    { "lin": 13, "col" : 1, "value" : "║  █│   │               █│               │  █│   │    █\_    │                                     ║" },
    { "lin": 14, "col" : 1, "value" : "║  █└───┘               █└───────────────┘  █└───┘     █ └───┘                                     ║" },
    { "lin": 15, "col" : 1, "value" : "║  ▀▀▀▀▀                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀▀                                      ║" },
    { "lin": 16, "col" : 1, "value" : "║                ┌───────────────┐    ┌───────────────┐    ┌───────────────┐    ┌───┐       ┌───┐  ║ " },
    { "lin": 17, "col" : 1, "value" : "║               █│               │   █│               │   █│               │   █│   │      █│   │  ║" },
    { "lin": 18, "col" : 1, "value" : "║               █└─────┐   ┌─────┘   █│   ┌───────────┘   █│   ┌───────────┘   █│   │      █│   │  ║" },
    { "lin": 19, "col" : 1, "value" : "║               ▀▀▀▀▀▀█│   │         █│   │▀▀▀▀▀▀▀▀▀▀▀    █│   │▀▀▀▀▀▀▀▀▀▀▀    █│   │      █│   │  ║" },
    { "lin": 20, "col" : 1, "value" : "║                     █│   │         █│   └────────┐      █│   │               █│   └───────┘   │  ║" },
    { "lin": 21, "col" : 1, "value" : "║                     █│   │         █│            │      █│   │               █│               │  ║" },
    { "lin": 22, "col" : 1, "value" : "║                     █│   │         █│   ┌────────┘      █│   │               █│   ┌───────┐   │  ║" },
    { "lin": 23, "col" : 1, "value" : "║                     █│   │         █│   │▀▀▀▀▀▀▀▀       █│   │               █│   │      █│   │  ║" },
    { "lin": 24, "col" : 1, "value" : "║                     █│   │         █│   └───────────┐   █│   └───────────┐   █│   │      █│   │  ║" },
    { "lin": 25, "col" : 1, "value" : "║                     █│   │         █│               │   █│               │   █│   │      █│   │  ║" },
    { "lin": 26, "col" : 1, "value" : "║                     █└───┘         █└───────────────┘   █└───────────────┘   █└───┘      █└───┘  ║" },
    { "lin": 27, "col" : 1, "value" : "║                     ▀▀▀▀▀          ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀       ▀▀▀▀▀   ║" },
    { "lin": 28, "col" : 1, "value" : "║                                                       Copyright by © André Rogério Bononi - 2025 ║" },
    { "lin": 29, "col" : 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin": 30, "col" : 1, "value" : "║                                                                                                  ║" },
    { "lin": 31, "col" : 1, "value" : "╚══════════════════════════════════════════════════════════════════════════════════════════════════╝" }
]

layout_cadastro_clientes = [
    { "lin":  5, "col" : 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col" : 1, "value" : "║ Código ..: [          ]     Pessoa:  ( ) FÍSICA   ( ) JURÍDICA    CPF/CNPJ: [                  ] ║" },
    { "lin":  9, "col" : 1, "value" : "║ Nome ....: [                                                                                   ] ║" },
    { "lin": 11, "col" : 1, "value" : "║ Endereço : [                                                                                   ] ║" },
    { "lin": 13, "col" : 1, "value" : "║ Número ..: [          ]       Complemento: [                                                   ] ║" },
    { "lin": 15, "col" : 1, "value" : "║ Bairro ..: [                                                                                   ] ║" },
    { "lin": 17, "col" : 1, "value" : "║ Cidade ..: [                                                                         ] UF.: [  ] ║" },
    { "lin": 19, "col" : 1, "value" : "║ CEP .....: [           ]       Telefone .: [             ]         Data Nacimento.: [          ] ║" },
    { "lin": 21, "col" : 1, "value" : "║ Situação : ( ) [A]TIVO ( ) [R]ESTRITO ( ) [B]LOQUEADO ( ) [I]NATIVO  Cliente Desde: [          ] ║" }
]

layout_cadastro_contas = [
    { "lin":  5, "col" : 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col" : 1, "value" : "║ Conta Nº.: [          ]     Tipo: ( ) CONTA CORRENTE  ( ) POUPANÇA  ( ) APLICAÇÃO                ║" },
    { "lin":  9, "col" : 1, "value" : "║ Cliente .: [                  ][                                                               ] ║" },
    { "lin": 11, "col" : 1, "value" : "║ Especial : [              ]                                          Data Abertura: [          ] ║" },
    { "lin": 13, "col" : 1, "value" : "║ Situação : ( ) ANALISE   ( ) ATIVA   ( ) SUSPENSA   ( ) BLOQUEADA   ( ) INATIVA   ( ) ENCERRADA  ║" },
    { "lin": 14, "col" : 1, "value" : "║                                                                      Encerrada em: [          ]  ║" },

]

layout_menu_transacoes = [
    { "lin":  5, "col": 1, "value": "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  9, "col": 1, "value": "║                ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐                 ║" },
    { "lin": 10, "col": 1, "value": "║                │   1 - DEPÓSITOS   │ │     2 - SAQUES    │ │     3 - PIX       │                 ║" },
    { "lin": 11, "col": 1, "value": "║                └───────────────────┘ └───────────────────┘ └───────────────────┘                 ║" },
    { "lin": 15, "col": 1, "value": "║                           ┌───────────────────┐  ┌───────────────────┐                           ║" },
    { "lin": 16, "col": 1, "value": "║                           │  4 - PAGAMENTOS   │  │ 5 - TRANFERÊNCIAS │                           ║" },
    { "lin": 17, "col": 1, "value": "║                           └───────────────────┘  └───────────────────┘                           ║" },
    { "lin": 21, "col": 1, "value": "║                                     ┌───────────────────┐                                        ║" },
    { "lin": 22, "col": 1, "value": "║                                     │     6 - DOCS      │                                        ║" },
    { "lin": 23, "col": 1, "value": "║                                     └───────────────────┘                                        ║" },
    { "lin": 26, "col": 1, "value": "║                                                                            ┌───────────────────┐ ║" },
    { "lin": 27, "col": 1, "value": "║                                                                            │     9 - SAIR      │ ║" },
    { "lin": 28, "col": 1, "value": "║                                                                            └───────────────────┘ ║" }
]

layout_menu_consultas = [
    { "lin":  5, "col": 1, "value": "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  8, "col": 1, "value": "║   ┌──────────────┐                                                                               ║" },
    { "lin":  9, "col": 1, "value": "║   │ 1 - CLIENTES │                                                                               ║" },
    { "lin": 10, "col": 1, "value": "║   └──────────────┘                                                                               ║" },
    { "lin": 12, "col": 1, "value": "║                      ┌──────────────┐                                                            ║" },
    { "lin": 13, "col": 1, "value": "║                      │  2 - CONTAS  │                                                            ║" },
    { "lin": 14, "col": 1, "value": "║                      └──────────────┘                                                            ║" },
    { "lin": 16, "col": 1, "value": "║                                         ┌──────────────┐                                         ║" },
    { "lin": 17, "col": 1, "value": "║                                         │  3 - SALDOS  │                                         ║" },
    { "lin": 18, "col": 1, "value": "║                                         └──────────────┘                                         ║" },
    { "lin": 20, "col": 1, "value": "║                                                            ┌──────────────┐                      ║" },
    { "lin": 21, "col": 1, "value": "║                                                            │ 4 - EXTRATOS │                      ║" },
    { "lin": 22, "col": 1, "value": "║                                                            └──────────────┘                      ║" },
    { "lin": 24, "col": 1, "value": "║                                                                               ┌──────────────┐   ║" },
    { "lin": 25, "col": 1, "value": "║                                                                               │ 9 - RETORNAR │   ║" },
    { "lin": 26, "col": 1, "value": "║                                                                               └──────────────┘   ║" }
]

layout_consulta_cliente = [
    { "lin":  4, "col": 1, "value" : "║ ( ) NOME  ( ) CPF/CNPJ ( ) CIDADE ( ) DATA NASCIMENTO   ARGUMENTO: [                           ] ║" },
    { "lin":  5, "col": 1, "value" : "╠════════════════════╦════════════════════════════════════╦═══════════════╦════════════╦═══════════╣" },
    { "lin":  6, "col": 1, "value" : "║ CPF/CNPJ           ║ NOME/RAZÃO SOCIAL                  ║   TELEFONE    ║ DATA NASC. ║   STATUS  ║" },
    { "lin":  7, "col": 1, "value" : "╠════════════════════╬════════════════════════════════════╬═══════════════╬════════════╬═══════════╣" },
    { "lin":  8, "col": 1, "value" : "║                    ║                                    ║               ║            ║           ║" },
    { "lin": 29, "col": 1, "value" : "╠════════════════════╩════════════════════════════════════╩═══════════════╩════════════╩═══════════╣" },
]

layout_opcoes_consultas = {
    "consulta_cliente" : { "lin": 4, "nome": 4, "cpf_cnpj": 14, "cidade": 27, "data_nascimento": 38 }
}