print('=' * 20, 'Loja da Beatriz', '=' * 20)
valor = float(input('Qual o valor do produto? '))
print("""Selecione a forma de pagamento
[1] - À vista em dinheiro ou em cheque
[2] - À vista no cartão
[3] - Em até 2x no cartão
[4] - 3x ou mais no cartão """)
opcao = int(input('Selecione o número da opção escolhida: '))
if opcao == 1:
    desconto1 = valor - (valor * 10 / 100)
    print('O valor de {} vai ser {:.2f}'.format(valor, desconto1))
elif opcao == 2:
    desconto2 = valor - (valor * 5 / 100)
    print('O valor de {} vai ser {:.2f}'.format(valor, desconto2))
elif opcao == 3:
    print('O valor vai ser {}'.format(valor))
    parcela = valor / 2
    print('O valor da compra {} vai ser parcelada em 2x de {:.2f}'.format(valor, parcela))
elif opcao == 4:
    desconto4 = valor + (valor * 20 / 100)
    total_de_parcelas = int(input('Quantas parcelas? '))
    parcelas = desconto4 / total_de_parcelas
    print('''
O valor de {}, parcelado em {}x 
vai custar cada parcela R${:.2f}, 
o valor no total vai ser R${:.2f},
COM JUROS DE 20%'''.format(valor, total_de_parcelas, parcelas, desconto4))
else:
    usuario = valor
    print('''
OPÇÃO INVÁLIDA de pagamento, 
tente novamente!,
o valor de {:.2f} vai custar {:.2f} no final'''.format(valor, usuario))






