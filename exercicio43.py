peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('\033[32m', 'Peso Ideal', '\033[m')
elif 25 <= imc < 30:
    print('\033[35m', 'Sobrepeso', '\033[m')
elif 30 <= imc < 40:
    print('\033[33m', 'Obesidade', '\033[m')
elif imc >= 40:
    print('\033[31m', 'Obesidade mórbida, cuidado', '\033[m')

