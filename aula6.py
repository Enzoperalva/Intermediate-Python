contador = 0
while True:   
    while contador <= 10:
        contador +=1
        print(contador)
        if contador == 4:
            continue
    
    cont = input('Deseja continuar [S/N]').strip().upper()[0]
    while cont not in 'SN':
        print('ERRO! Tente novamente.')
        cont = input('Deseja continuar [S/N]').strip().upper()[0]
    if cont == 'N':
        break
    else:
        contador = 0
