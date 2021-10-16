metros = int(input('Digite um valor: '))
metros1 = (metros) * 10 ** 0
centimetros = (metros) * 10 ** -2
milimetros = (metros) * 10 ** -3
print('Esse número em metros é = {}{}{}m\nEm centímetros é = {}cm\nEm milímetros = {}mm'.format('\033[31m', metros1, centimetros, milimetros, '\033[m'))



