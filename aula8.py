x = contador_vogal = 0
vogais = 'aeiou'
letra_atual = ''
letra_ja_vista = ''

name = input('Nome: ').strip().lower()
while True:
    letra_atual = name[x]
    if letra_atual in vogais:
        if letra_atual not in letra_ja_vista:
            contador_vogal += 1
            letra_ja_vista += letra_atual
    x += 1
    if x == len(name):
        break
if contador_vogal > 0:
    print(f'{name} tem {contador_vogal} vogais que não se repetem!')
else:
    print(f'{name} não tem vogal')