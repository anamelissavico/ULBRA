plano= int(input("Olá qual plano você gostaria de assinar?\n [1] musculação\n [2] musculação + funcional\n [3] crossfit\n"))

if plano==1:
    dias_semana=input(f'Os planos de musculação tem as seguintes frequências:\n [1] 2 dias na semana\n [2] 3 dias na semana \n [3] livre\n Que plano você gostaria de assinar?\n')
    if dias_semana==1:
        print(f'O valor do plano é 80 reais.')
    elif dias_semana==2:
        print(f'O valor do plano é 100 reais.')
    elif dias_semana==3:
        print(f'O valor do plano é 120 reais.')
    else:
        print(f'Não tem essa opção, digite uma das opções acima.')

elif plano==2:
    dias_semana=input(f'Os planos de musculação + funcional tem as seguintes frequências:\n [1] 2 dias na semana\n [2]3 dias na semana \n [3] livre\n Que plano você gostaria de assinar?\n')
    if dias_semana==1:
        print(f'O valor do plano é 120 reais.')
    elif dias_semana==2:
        print(f'O valor do plano é 140 reais.')
    elif dias_semana==3:
        print(f'O valor do plano é 170  reais.')
    else:
        print(f'Não tem essa opção, digite uma das opções acima.')
elif plano==3:
    dias_semana=input(f'Os planos de crossfit tem as seguintes frequências:\n [1] 2 dias na semana\n [2]3 dias na semana \n [3] livre\n Que plano você gostaria de assinar?')
    if dias_semana==1:
        print(f'O valor do plano é 120 reais.')
    elif dias_semana==2:
        print(f'O valor do plano é 160 reais.')
    elif dias_semana==3:
        print(f'O valor do plano é 200 reais.')
    else:
        print(f'Não tem essa opção, digite uma das opções acima.')
else:
    print(f'Não tem essa opção, digite uma das opções acima.')
print(f'Obrigada por escolher a gente, bom treino!!!!')
