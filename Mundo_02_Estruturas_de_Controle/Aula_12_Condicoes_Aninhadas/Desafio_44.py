'''
Desafio 44 (24:36): Calcule o valor a ser pago por um produto, considerando o preço normal e a condição de pagamento:
à vista no dinheiro/cheque (10% de desconto), à vista no cartão (5% de desconto), em até 2x no cartão (preço normal)
ou 3x ou mais no cartão (20% de juros).
'''

cores = {
    # Reset
    'limpa': '\033[m',

    # Cores normais
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    # Cores claras / brilhantes
    'cinza': '\033[90m',
    'vermelhoclaro': '\033[91m',
    'verdeclaro': '\033[92m',
    'amareloclaro': '\033[93m',
    'azulclaro': '\033[94m',
    'magentaclaro': '\033[95m',
    'cianoclaro': '\033[96m',
    'brancoclaro': '\033[97m',

    # Estilos
    'negrito': '\033[1m',
    'fraco': '\033[2m',
    'sublinhado': '\033[4m',
    'piscando': '\033[5m',
    'invertido': '\033[7m',

    # Combinações
    'pretoebranco': '\033[7;97m',
}

valor_a_ser_pago = float(input("Digite o valor do produto: "))
print('''\nDigite (1) para pagamento à vista no dinheiro ou cheque
Digite (2) para pagar à vista no cartão
Digite (3) para pagamento no cartão em até 2x
Digite (4) para pagamento no cartão em 3x ou mais''')
opcoes_de_pagamento = int(input("\nOpção de pagamento: "))

if opcoes_de_pagamento == 1:
    desconto_10_por_cento = valor_a_ser_pago - (valor_a_ser_pago * 10 / 100)
    print(f'''\nVocê escolheu a {cores['verde']}opção (1){cores['limpa']} para pagar em à vista no dinheiro ou cheque.
Você tem direito a {cores['verde']}10% de desconto{cores['limpa']}.
O seu produto que custava {cores['verde']}R$ {valor_a_ser_pago:.2f}{cores['limpa']} passa a custar {cores['verde']}
R$ {desconto_10_por_cento:.2f}.{cores['limpa']}''')
elif opcoes_de_pagamento == 2:
    desconto_5_por_cento = valor_a_ser_pago - (valor_a_ser_pago * 5 / 100)
    print(f'''\nVocê escolheu a {cores['verde']}opção (2){cores['limpa']} para pagar à vista no cartão.
Você tem direito a a {cores['verde']}5% de desconto{cores['limpa']}. O seu produto que custava {cores['verde']}
R$ {valor_a_ser_pago:.2f}{cores['limpa']} passa a custar {cores['verde']}R$ {desconto_5_por_cento:.2f}{cores['limpa']}.''')
elif opcoes_de_pagamento == 3:
    parcelamento_do_valor = valor_a_ser_pago / 2
    print(f'''\nVocê escolheu a {cores['verde']}opção (3){cores['limpa']}.
O seu pagamento será dividido em {cores['verde']}2 vezes{cores['limpa']} 
de {cores['verde']}R$ {parcelamento_do_valor:.2f}{cores['limpa']}.''')
elif opcoes_de_pagamento == 4:
    parcelas = int(input("\nEscolha em quantas vezes deseja parcelar o produto: "))
    if parcelas < 3:
        print(f"{cores['vermelho']}ERRO. Digite um parcelamento em 3 ou acima de 3 vezes.{cores['vermelho']}")
    else:
        taxa_de_20_por_cento_de_juros = valor_a_ser_pago + (valor_a_ser_pago * 20 / 100)
        valor_parcelado = taxa_de_20_por_cento_de_juros / parcelas
        print(f'''\nVocê escolheu a {cores['verde']}opção (4){cores['limpa']} para pagamento no cartão em 3x ou mais.
O seu produto passa a ter uma {cores['verde']}taxa de 20% de juros{cores['limpa']}.
O seu produto que custava {cores['verde']}R$ {valor_a_ser_pago:.2f}{cores['limpa']} passa a custar {cores['verde']}
R$ {taxa_de_20_por_cento_de_juros:.2f}{cores['limpa']}.   
Ele será dividido em {cores['verde']}{parcelas} parcelas{cores['limpa']} de {cores['verde']}R$ {valor_parcelado:.2f}{cores['limpa']}.''')
