sexo=input('Você é do sexo feminino ou masculino?\n')
altura=float(input('Qual é sua altura?\n'))

if sexo=="masculino":
    peso_ideal= (72.7*altura)-58
    print (f'Seu peso ideal é {peso_ideal}kg')
else:
    peso_ideal= (62.1*altura)-44.7
    print(peso_ideal)