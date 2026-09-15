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
print('''Digite (1) para pagamento à vista em dinheiro/cheque
Digite (2) para pagar à vista no cartão
Digite (3) para pagamento no cartão em até 2x
Digite (4) para pagamento no cartão em 3x ou mais''')
opcoes_de_pagamento = int(input("Opção de pagamento: "))

if opcoes_de_pagamento == 1:
    desconto_10_por_cento = valor_a_ser_pago - (valor_a_ser_pago * 10 / 100)
    print(f'''Você escolheu a opção (1) para pagar em dinheiro ou cheque.
Você tem direito a 10% de desconto.
O seu produto que custava R$ {valor_a_ser_pago:.2f} passa a custar R$ {desconto_10_por_cento:.2f}''')
elif opcoes_de_pagamento == 2:
    desconto_5_por_cento = valor_a_ser_pago - (valor_a_ser_pago * 5 / 100)
    print(f'''Você escolheu a opção (2) para pagar à vista no cartão.
Você tem direito a a 5% de desconto.
O seu produto que custava R$ {valor_a_ser_pago:.2f} passa a custar R$ {desconto_5_por_cento:.2f}''')
elif opcoes_de_pagamento == 3:
    print(f'''Você escolheu a opção (3) para pagamento no cartão em até 2x.
O seu produto custa R$ {valor_a_ser_pago:.2f}''')
elif opcoes_de_pagamento == 4:
    taxa_de_20_por_cento_de_juros = valor_a_ser_pago + (valor_a_ser_pago * 20 / 100)
    print(f'''Você escolheu a opção (4) para pagamento no cartão em 3x ou mais.
O seu produto passa a ter uma taxa de 20% de juros.    
O seu produto que custava R$ {valor_a_ser_pago:.2f} passa a custar R$ {taxa_de_20_por_cento_de_juros:.2f}''')
