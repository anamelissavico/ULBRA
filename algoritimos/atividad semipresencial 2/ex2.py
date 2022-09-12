numero=int(input('Digite seu número\n'))
horas=float(input('Quantas horas você trabalhou esse mês?\n'))
valor_hora=float(input('Quanto você recebe por hora trabalhada?\n'))
filhos=int(input('Quantos filhos menores de 14 você tem?\n'))
idade=int(input('Digite a idade do/s seu/s filh@/s\n'))
tempo=float(input('Há quanto tempo você trabalha na empresa?\n'))

sb=horas*valor_hora
sf=filhos*56.47
inss=sb*0.085
sb_limpo=sb-inss

if sb>1500:
    ir=sb_limpo*0.15
    print(f'Seu salário é igual a {sb_limpo} reais e seu Imposto de renda é {ir} reais.')
elif sb<=1500 and sb>500:
    ir=sb_limpo*0.8
    print(f'Seu salário é igual a {sb_limpo} reais e seu Imposto de renda é {ir} reais.')
else:
    ir=0
    print(f' Seu salário é igual a {sb_limpo} reais e você não possui imposto de renda.')