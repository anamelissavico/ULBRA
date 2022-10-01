peso_atual=float(input('Olá\n Informe seu peso:\n'))
liquidos_ult_24hs=float(input('Informe a quantidade de líquidos em litros que você bebeu nas últimas 24 horas:'))

peso_seco= peso_atual-liquidos_ult_24hs
dif= peso_atual - peso_seco

print(f'A diferença entre seu peso e seu peso seco é {dif}.')

if dif>1 and dif<2:
    print(f' Você deverá ficar 2h na hemodiálise.')
elif dif>2 and dif<3:
    print(f'Você deverá ficar 3h na hemodiálise.')
elif dif>3:
    print (f'Você deverá ficar 4h na hemodiálise.')