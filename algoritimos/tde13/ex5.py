print(f'****************************************************************')

print(f'Olá seja bem vindo, vamos escolher o seu futuro carro?')

valor_carro=float(input('Digite o valor do carro:\n'))

print(f'****************************************************************')

parcelas=float(input('Os valores e  opções de parcelas serão listados abaixo:\n [1] 6 x   com acréscimo de 3%\n [2] 12 x  com acréscimo de 6%\n [3] 18 x  com acréscimo de 9%\n [4] 24 x  com acréscimo de 12%\n [5] 30 x  com acréscimo de 15%\n [6] 36 x   com acréscimo de 18%\n [7] 42 x  com acréscimo de 21%\n [8] 48 x    com acréscimo de 24%\n [9] 54 x  com acréscimo de 27%\n [10] 60 x    com acréscimo de 30%\n Infome a opção de parcela que você deseja segundo o número.\n'))

if parcelas==1:
    valor_total=valor_carro+valor_carro*0.03
    print(f'Você escolheu pagar em 6 parcelas')
elif parcelas==2:
    valor_total=valor_carro+valor_carro*0.06
    print(f'Você escolheu pagar em 12 parcelas')
elif parcelas==3:
    valor_total=valor_carro+valor_carro*0.09
    print(f'Você escolheu pagar em 18 parcelas')
elif parcelas==4:
    valor_total=valor_carro+valor_carro*0.12
    print(f'Você escolheu pagar em 24 parcelas')
elif parcelas==5:
    valor_total=valor_carro+valor_carro*0.15
    print(f'Você escolheu pagar em 30 parcelas')
elif parcelas==6:
    valor_total=valor_carro+valor_carro*0.18
    print(f'Você escolheu pagar em 36 parcelas')
elif parcelas==7:
    valor_total=valor_carro+valor_carro*0.21
    print(f'Você escolheu pagar em 42 parcelas')
elif parcelas==8:
    valor_total=valor_carro+valor_carro*0.24
    print(f'Você escolheu pagar em 48 parcelas')
elif parcelas==9:
    valor_total=valor_carro+valor_carro*0.27
    print(f'Você escolheu pagar em 54 parcelas')
elif parcelas==10:
    valor_total=valor_carro+valor_carro*0.30
    print(f'Você escolheu pagar em 60 parcelas')


print(f'****************************************************************')

cond_pagamento=float(input('Agora você deve escolher a condição de pagamento que deseja:\n [1] Á vista (desconto de 20%)\n [2] No crédito\n [3] No boleto\n '))
if cond_pagamento==1:
   valor_final=valor_total-(valor_total*0.20)

print(f'O valor total do seu carro é {valor_final}reais, muito obrida por escolher nossa concessionária! ')