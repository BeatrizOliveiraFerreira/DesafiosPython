frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('\033[45m', frase.find('A')+1, '\033[m')
print(frase.rfind('A')+1)






