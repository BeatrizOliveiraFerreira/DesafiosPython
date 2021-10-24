times = ('Atlético-MG', 'Fortaleza EC', 'Flamengo',
        'Palmeiras', 'Bragantino', 'Internacional',
        'Corinthians', 'Fluminense', 'América-MG',
        'Cuiabá', 'Athletico-PR', 'Atlético Goianiense',
        'São Paulo', 'Ceará', 'Juventude', 'Santos',
        'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print('-=' * 30)
print(f'Lista de times {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')


