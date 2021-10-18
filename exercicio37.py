numero = int(input('Digite um número: '))
print("""Qual será a base de conversão?
[1]- para BINÁRIO
[2] - para OCTAL
[3] - para HEXADECIMAL """)
opcao = int(input('Digite um desses três números: '))
if opcao == 1:
    print('{} Convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, digite uma das opções')

