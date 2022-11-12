casas_entrevistadas=0
canal_4=0
canal_5=0
canal_7=0
canal_12=0
x=1

while x >0:
    canal=int(input('Que canal você está assistindo?\n [1] Canal 4\n [2] Canal 5\n [3] Canal 7\n [4] Canal 12\n'))
    pessoas_assistindo=int(input('Quantas pessoas estão assistindo tv na sua casa agora?\n'))

    if canal==1:
        canal_4+=pessoas_assistindo
        casas_entrevistadas=casas_entrevistadas+pessoas_assistindo
    elif canal==2:
        canal_5+=pessoas_assistindo
        casas_entrevistadas=casas_entrevistadas+pessoas_assistindo
    elif canal==3:
        canal_7+=pessoas_assistindo
        casas_entrevistadas=casas_entrevistadas+pessoas_assistindo
    elif canal==4:
        canal_12+=pessoas_assistindo
        casas_entrevistadas=casas_entrevistadas+pessoas_assistindo
    elif canal==0:
        x=0

print(f'{(canal_4*100/casas_entrevistadas)}% das pessoas estão assistindo o Canal 4.\n'
f'{(canal_5*100/casas_entrevistadas)}% das pessoas estão assistindo o Canal 5.\n'
f'{(canal_7*100/casas_entrevistadas)}% das pessoas estão assistindo o Canal 7.\n'
f'{(canal_12*100/casas_entrevistadas)}% das pessoas estão assistindo o Canal 12.\n')
