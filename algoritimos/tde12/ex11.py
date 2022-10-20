for i in range (5):
    n1=float(input('Digite sua nota\n'))
    n2=float(input('Digite sua nota\n'))
    n3=float(input('Digite sua nota\n'))
    media=(n1+n2+n3)/3
    if media>=7:
        print(f'Você foi aprovado.')
    else:
        print(f'Você foi reprovado.')