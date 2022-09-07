nota_ps=float(input('Digite sua nota\n'))
if nota_ps>=6:
    print('Você foi aprovado!')
    print('Parabéns\n')
    if nota_ps>9:
        print('Vcoê é demais')
elif nota_ps<6 and nota_ps>4:
    print("Você pegou exame :(")
    print("Sem pizza galera")
else:
    print('Você não foi aprovado\n')
print(f'Sua nota é {nota_ps}')