x=0
total_idade=0
pessoas=0
idade=0


while idade>=0:
    idade=int(input('Digite sua idade:\n'))
    if idade>0:
        pessoas=pessoas+1
        total_idade+=idade
    else:
        break
    
print(f'A média das idades é {total_idade/pessoas}')