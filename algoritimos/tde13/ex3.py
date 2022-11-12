qtde_pessoas_50=0
qtde_pessoas_10_20=0
soma_pessoas_10_20=0
pessoas_peso_40=0

for i in range(3):
    altura=int(input('Digite sua altura em centimetros:\n'))
    peso=float(input('Digite seu peso:\n'))
    idade=int(input('Digite sua idade:\n'))

    if idade>50:
        qtde_pessoas_50+=1
    if idade>10 and idade<20:
        qtde_pessoas_10_20+=1
        soma_pessoas_10_20+=altura
    if peso<10:
        pessoas_peso_40+=1
print(f'O número de pessoas com 50 anos é {qtde_pessoas_50}')
print(f' a média de alturas das pessoas entre 10 e 20 anos é {soma_pessoas_10_20/qtde_pessoas_10_20}')