from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {n}')
print(f'O maior valor sorteado foi o {max(n)}')
print(f'O menor valor sorteado foi o {min(n)}')


