dias = int(input('Quantos dias alugados? '))
quilometros = float(input('Quantos Km rodados? '))
precoDias = 60.0
precoQuilometro = 0.15
resultado = (dias * precoDias) + (quilometros * precoQuilometro)
print('O preço a pagar é: R${}{:.2f}{}'.format('\033[33m', resultado, '\033[m'))







