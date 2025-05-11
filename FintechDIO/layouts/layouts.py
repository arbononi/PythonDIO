opcoes_disponiveis = {
    "menu_principal" : "[1 - CLIENTES]      [2 - CONTAS]      [3 - TRANSAÇÕES]      [4 - CONSULTAS]      [9 - SAIR]".center(98, " "),
    "opcoes_cadastro" : "[C]ONSULTAR        [I]NCLUIR        [A]LTERAR        [E]XCLUIR        [L]ISTAR        [R]ETORNAR".center(98, " "),
    "opcoes_transacao" : "[1]-DEPÓSITO   [2]-SAQUE   [3]-PIX   [4]-PAGAMENTO   [5]-TRANSFERÊNCIA   [6]-DOC   [9]-SAIR".center(98, " "),
    "menu_consultas" : " Escolha dentre as opções disponíveis: S = SALDOS, E = EXTRATOS ou R = RETORNAR",
    "opcoes_consultas" : "[N]OVA CONSULTA             [P]RÓXIMA PÁGINA             [V]OLTAR PÁGINA             [R]ETORNAR".center(98, " "),
    "consulta_saldo" : "Digite 0 (zero) no número da conta para encerrar",
    "consulta_conta" : "[N]OVA CONSULTA                         [G]ERENCIAR CHAVES PIX                        [R]ETORNAR".center(98, " "),
    "gerencia_chavespix": "[C]ADATRAR CHAVE PIX                     [E]XCLUIR CHAVE PIX                          [R]ETORNAR".center(98, " ")
}

titulo_telas = {
    "menu_principal" : "FINTECHDIO - SISTEMA FINANCEIRO - MENU PRINCIPAL".center(75, " "),
    "cadastro_clientes" : "CADASTRO DE CLIENTES".center(98, " "),
    "cadastro_contas" : "CADASTRO DE CONTAS".center(98, " "),
    "transacoes" : "OPERAÇÕES  BANCÁRIAS".center(98, " "),
    "titulo_consultas" : "CONSULTA SALDOS/EXTRATOS".center(98, " "),
    "consulta_cliente" : "CONSULTA DE CLIENTES".center(75, " "),
    "consulta_conta" : "CONSULTA DE CONTAS".center(98, " "),
    "consulta_saldo" : "CONSULTA SALDO".center(98, " "),
    "consulta_extratos" : "CONSULTA EXTRATOS".center(75, " "),
    "gerencia_chavespix": "FINTECHDIO - SISTEMA FINANCEIRO - GERENCIAMENTO DE CHAVES PIX".center(75, " ")
}

operacoes_disponiveis = {
    "menu_principal" : [ 1, 2, 3, 4, 9 ],
    "operacoes_cadastro" : [ "C", "I", "A","E", "L", "R" ],
    "operacoes_transacao" : [ 1, 2, 3, 4, 5, 6, 9 ],
    "menu_consultas" : [ "S", "E", "R" ],
    "opcoes_consultas" : [ "N", "P", "V", "R" ],
    "consulta_conta" : [ "N", "G", "R"],
    "gerencia_chavespix": [ "C", "E", "R" ]
}

layout_menu_principal = [
    { "lin":  1, "col" : 1, "value" : "╔═══════════════════════════════════════════════════════════════════════════╦══════════════════════╗" },
    { "lin":  2, "col" : 1, "value" : "║                                                                           ║ Data:                ║" },
    { "lin":  3, "col" : 1, "value" : "╠═══════════════════════════════════════════════════════════════════════════╩══════════════════════╣" },
    { "lin":  4, "col" : 1, "value" : "║                                                                                                  ║" },
    { "lin":  5, "col" : 1, "value" : "║  ███████████████╗ ████████████████╗ ████╗       ████╗                                            ║" },
    { "lin":  6, "col" : 1, "value" : "║  ███████████████║ ████████████████║ █████       ████║                                            ║" },
    { "lin":  7, "col" : 1, "value" : "║  ████╔══════════╝ ╚═════████╔═════╝ ██████      ████║                                            ║" },
    { "lin":  8, "col" : 1, "value" : "║  ████║                  ████║       ███████     ████║                                            ║" },
    { "lin":  9, "col" : 1, "value" : "║  ████████████╗          ████║       ████║████   ████║                                            ║" },
    { "lin": 10, "col" : 1, "value" : "║  ████████████║          ████║       ████║  ████ ████║                                            ║" },
    { "lin": 11, "col" : 1, "value" : "║  ████╔═══════╝          ████║       ████║    ███████║                                            ║" },
    { "lin": 12, "col" : 1, "value" : "║  ████║                  ████║       ████║     ██████║                                            ║" },
    { "lin": 13, "col" : 1, "value" : "║  ████║            ████████████████╗ ████║      █████║                                            ║" },
    { "lin": 14, "col" : 1, "value" : "║  ████║            ████████████████║ ████║       ████║                                            ║" },
    { "lin": 15, "col" : 1, "value" : "║  ╚═══╝            ╚═══════════════╝ ╚═══╝       ╚═══╝                                            ║" },
    { "lin": 16, "col" : 1, "value" : "║                                                                                                  ║" },
    { "lin": 17, "col" : 1, "value" : "║                           ████████████████╗ ███████████████╗ ███████████████╗ ████╗       ████╗  ║" },
    { "lin": 18, "col" : 1, "value" : "║                           ████████████████║ ███████████████║ ███████████████║ ████║       ████║  ║" },
    { "lin": 19, "col" : 1, "value" : "║                                 ████╔═════╝ ████╔══════════╝ ████╔══════════╝ ████║       ████║  ║" },
    { "lin": 20, "col" : 1, "value" : "║                                 ████║       ████║            ████║            ████║       ████║  ║" },
    { "lin": 21, "col" : 1, "value" : "║                                 ████║       ████████████╗    ████║            ████████████████║  ║" },
    { "lin": 22, "col" : 1, "value" : "║                                 ████║       ████████████║    ████║            ████████████████║  ║" },
    { "lin": 23, "col" : 1, "value" : "║                                 ████║       ████╔═══════╝    ████║            ████╔═══════████║  ║" },
    { "lin": 24, "col" : 1, "value" : "║                                 ████║       ████║            ████║            ████║       ████║  ║" },
    { "lin": 25, "col" : 1, "value" : "║                                 ████║       ███████████████╗ ███████████████╗ ████║       ████║  ║" },
    { "lin": 26, "col" : 1, "value" : "║                                 ████║       ███████████████║ ███████████████║ ████║       ████║  ║" },
    { "lin": 27, "col" : 1, "value" : "║                                 ╚═══╝       ╚══════════════╝ ╚══════════════╝ ╚═══╝       ╚═══╝  ║" },
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
    { "lin": 19, "col" : 1, "value" : "║ CEP .....: [          ]        Telefone .: [             ]        Data Nascimento.: [          ] ║" },
    { "lin": 21, "col" : 1, "value" : "║ Situação : ( ) [A]TIVO ( ) [R]ESTRITO ( ) [B]LOQUEADO ( ) [I]NATIVO  Cliente Desde: [          ] ║" }
]

layout_cadastro_contas = [
    { "lin":  5, "col" : 1, "value" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col" : 1, "value" : "║ Conta Nº.: [          ]     Tipo: ( ) CONTA CORRENTE  ( ) POUPANÇA  ( ) APLICAÇÃO                ║" },
    { "lin":  9, "col" : 1, "value" : "║ Cliente .: [                  ][                                                               ] ║" },
    { "lin": 11, "col" : 1, "value" : "║ Especial : [              ]                                          Data Abertura: [          ] ║" },
    { "lin": 13, "col" : 1, "value" : "║ Situação : ( ) ANALISE   ( ) ATIVA   ( ) SUSPENSA   ( ) BLOQUEADA   ( ) INATIVA   ( ) ENCERRADA  ║" },
    { "lin": 15, "col" : 1, "value" : "║                                                                      Encerrada em: [          ]  ║" },

]

layout_transacoes = [
    { "lin":  5, "col": 1, "value": "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col": 2, "value": " ( ) DEPÓSITO      ( ) SAQUE      ( ) PIX      ( ) PAGAMENTO      ( ) TRANSFERÊNCIA      ( ) DOC  " },
    { "lin":  9, "col": 2, "value": " Conta Origem ..: [          ][                  ][                                             ] " },
    { "lin": 11, "col": 2, "value": " Conta Destino .: [          ][                  ][                                             ] " },
    { "lin": 13, "col": 2, "value": " Tipo de Chave .: ( ) CPF      ( ) CNPJ      ( ) TELEFONE      ( ) EMAIL      ( ) CHAVE ALEATORIA " },
    { "lin": 15, "col": 2, "value": " Chave Pix .....: [                                                                             ] " },
    { "lin": 17, "col": 2, "value": " Linha Digitável: [                                                                             ] " },
    { "lin": 19, "col": 2, "value": " Valor Operação : [              ] Nome do Autor: [                                             ] " },
    { "lin": 21, "col": 2, "value": " Mensagem ......: [                                                                             ] " },
    { "lin": 28, "col": 2, "value": " Confirma os Dados (S/N)?                 OBS: Operação não poderá ser revertida após confirmação " }
]

layout_consultas = [
    { "lin":  5, "col": 1, "value": "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  7, "col": 1, "value": "║  ┌────────────┐                                                                                  ║" },
    { "lin":  8, "col": 1, "value": "║  │  [S]ALDOS  │                                                                                  ║" },
    { "lin":  9, "col": 1, "value": "║  └────────────┘                                                                                  ║" },
    { "lin": 16, "col": 1, "value": "║                                          ┌────────────┐                                          ║" },
    { "lin": 17, "col": 1, "value": "║                                          │ [E]XTRATOS │                                          ║" },
    { "lin": 18, "col": 1, "value": "║                                          └────────────┘                                          ║" },
    { "lin": 25, "col": 1, "value": "║                                                                                  ┌────────────┐  ║" },
    { "lin": 26, "col": 1, "value": "║                                                                                  │ [R]ETORNAR │  ║" },
    { "lin": 27, "col": 1, "value": "║                                                                                  └────────────┘  ║" },
]

layout_consulta_cliente = [
    { "lin":  4, "col": 1, "value" : "║ ( ) NOME  ( ) CPF/CNPJ ( ) CIDADE ( ) DATA NASCIMENTO   ARGUMENTO: [                           ] ║" },
    { "lin":  5, "col": 1, "value" : "╠════════════════════╦════════════════════════════════════╦═══════════════╦════════════╦═══════════╣" },
    { "lin":  6, "col": 1, "value" : "║ CPF/CNPJ           ║ NOME/RAZÃO SOCIAL                  ║   TELEFONE    ║ DATA NASC. ║   STATUS  ║" },
    { "lin":  7, "col": 1, "value" : "╠════════════════════╬════════════════════════════════════╬═══════════════╬════════════╬═══════════╣" },
    { "lin":  8, "col": 1, "value" : "║                    ║                                    ║               ║            ║           ║" },
    { "lin": 29, "col": 1, "value" : "╠════════════════════╩════════════════════════════════════╩═══════════════╩════════════╩═══════════╣" },
]

layout_consulta_conta = [
    { "lin":  5, "col": 1, "value": "╠════════════╦════════════════════════════════════════════╦═══════════════╦════════════╦═══════════╣" },
    { "lin":  6, "col": 1, "value": "║   NÚMERO   ║ NOME/RAZÃO SOCIAL DO CLIENTE               ║   TELEFONE    ║  ABERTURA  ║   STATUS  ║" },
    { "lin":  7, "col": 1, "value": "╠════════════╬════════════════════════════════════════════╬═══════════════╬════════════╬═══════════╣" },
    { "lin":  8, "col": 1, "value": "║            ║                                            ║               ║            ║           ║" },
    { "lin": 29, "col": 1, "value": "╠════════════╩════════════════════════════════════════════╩═══════════════╩════════════╩═══════════╣" }

]

layout_opcoes_consultas = {
    "consulta_cliente" : { "lin": 4, "nome": 4, "cpf_cnpj": 14, "cidade": 27, "data_nascimento": 38 }
}

layout_consulta_saldo = [
    { "lin": 5, "col": 1, "value": "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin": 7, "col": 1, "value": "║ Conta Nº: [          ][                  ][                                                    ] ║" },
    { "lin": 9, "col": 1, "value": "║ Saldo ..: [               ]   Limite Especial.: [              ]   Disponível: [               ] ║" }
]

layout_consulta_extratos = [
    { "lin":  4, "col": 1, "value": "║ Conta Nº: [          ][                                ] PERIODO DE: [          ] A [          ] ║" },
    { "lin":  5, "col": 1, "value": "╠═════════════════════╦═════════════════╦════════════════╦═════════════════╦═════════════════╦═════╣" },
    { "lin":  6, "col": 1, "value": "║    DATA      HORA   ║ SALDO  ANTERIOR ║ VALOR OPERACAO ║   SALDO FINAL   ║    TRANSAÇÃO    ║ D/C ║" },
    { "lin":  7, "col": 1, "value": "╠═════════════════════╬═════════════════╬════════════════╬═════════════════╬═════════════════╬═════╣" },
    { "lin":  8, "col": 1, "value": "║                     ║                 ║                ║                 ║                 ║     ║" },
    { "lin": 29, "col": 1, "value": "╠═════════════════════╩═════════════════╩════════════════╩═════════════════╩═════════════════╩═════╣" }
]

layout_gerencia_chavespix = [
    { "lin":  4, "col": 1, "value": "║ CONTA Nº: [          ][                  ][                                                    ] ║" },
    { "lin":  5, "col": 1, "value": "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  6, "col": 1, "value": "║ TIPO DE CHAVE: ( ) CPF      ( ) CNPJ      ( ) TELEFONE      ( ) EMAIL      ( ) CHAVE ALEATORIA   ║" },
    { "lin":  7, "col": 1, "value": "║ CHAVE .......: [                                             ]        CONFIRMA OS DADOS (S/N):   ║" },
    { "lin":  8, "col": 1, "value": "╠═════╦═════════════════╦══════════════════════════════════════════════════════════════════════════╣" },
    { "lin":  9, "col": 1, "value": "║ SEQ ║  TIPO DE CHAVE  ║ IDENTIFICAÇÃO DA CHAVE                                                   ║" },
    { "lin": 10, "col": 1, "value": "╠═════╬═════════════════╬══════════════════════════════════════════════════════════════════════════╣" },
    { "lin": 11, "col": 1, "value": "║     ║                 ║                                                                          ║" }
]

restaurar_linha = {
    "linha_vazia" : "║                                                                                                  ║", 
    "separadora" : "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣"
}

restaurar_linha_29 = "╠══════════════════════════════════════════════════════════════════════════════════════════════════╣"