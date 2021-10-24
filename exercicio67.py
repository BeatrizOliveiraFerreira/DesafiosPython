while True:
    n = int(input('Qual valor você quer calcular? '))
    if n < 0:
        break
    for c in range(0, 11):
        resultado = n * c
        print(f'{n} x {c} = {resultado}')
print('Programa Encerrado, Volte Sempre!!')





