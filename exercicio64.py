numero = 0
cont = 0
soma = 0
numero = int(input('Digite um número [999] para parar: '))
while numero != 999:
    soma = soma + numero
    cont = cont + 1
    numero = int(input('Digite um número [999] para parar: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

