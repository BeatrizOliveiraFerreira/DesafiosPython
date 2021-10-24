total18 = total_de_homens = total_de_mulheres_com_menos_de_20_anos = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/f]? ')).strip().upper()[0]
    if idade >= 18:
        total18 = total18 + 1
    if sexo == 'M':
        total_de_homens = total_de_homens + 1
    if sexo == 'F' and idade < 20:
        total_de_mulheres_com_menos_de_20_anos = total_de_mulheres_com_menos_de_20_anos + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {total_de_homens} homens cadastrados')
print(f'E temos {total_de_mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos')





