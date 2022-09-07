conta=int(input(f'Digite o número da sua conta:\n'))
saldo=float(input('Digite o saldo da sua conta:\n'))
if saldo<0:
    print(f'CONTA ESTOURADA')
else:
    print(f'CONTA NORMAL')