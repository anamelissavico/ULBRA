total_salarios=0
pessoas_entrevistadas=0
x=0
maior_salario=0
menor_salario=1

pessoas_salario_200=0
sexo_pessoa_menor_salario=''
idade_pessoa_menor_salario=0
idade=0

while idade>=0:

    idade=int(input('Informe sua idade:\n'))
    sexo=input('Qual é o seu sexo: [F] Feminino ou [M] Masculino:\n')
    salario=float(input('Informe seu salario:\n'))
    total_salarios+=salario
    pessoas_entrevistadas+=1
    if idade==0:
        menor_idade==idade
        maior_idade==idade
        if idade>maior_idade:
            maior_idade=idade
        elif idade<=0:
            menor_idade=idade
        elif idade<menor_idade:
            menor_idade=idade
    if salario==0:
        menor_idade==idade
        maior_idade=idade
        if salario<200 and sexo=='f':
            pessoas_salario_200+=1
        if salario>maior_salario:
            maior_salario==salario
        elif salario<menor_salario:
            menor_salario=salario
    
print(f'A média de salários do grupo é {total_salarios/pessoas_entrevistadas}')
print(f'A maior idade é {maior_idade} e a menor idade é {menor_idade}')
print(f'O número de mulheres com salário menor que até 200 reais é {pessoas_salario_200}')
print(f'A idade da pessoa com menor salário é {idade_pessoa_menor_salario} e o sexo é {sexo_pessoa_menor_salario}')