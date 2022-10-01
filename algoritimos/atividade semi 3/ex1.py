nome=input('Seja bem vindo ao Sistema de Alistamento Militar!\n [1] Informe seu nome:\n')
rg=int(input('[2] Informe seu RG:\n'))
cpf=int(input('[3] Informe seu CPF:\n'))

comorbidade=int(input('Você possui alguma comorbidade/doença?\n [1] Sim\n [2] Não\n'))

if comorbidade==1:
    doenca=input('Qual?\n')
    print(f'{nome} tendo em vista que você possui {doenca}, você está dispensado do serviço militar obrigatório. Muito obrigada!')
else:
    print(f'Parabéns {nome} você foi aceito, e a partir deste momento você presta serviços para o Exercito Brasileiro, seja bem vindo!')