numero = soma = quantidade = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    quantidade = quantidade + 1
    soma = soma + numero
print(f'A quantidade de números digitados foi {quantidade} e a soma entre eles foi {soma}')


