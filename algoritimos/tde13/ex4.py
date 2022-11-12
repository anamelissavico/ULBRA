
x=0
p_alt_menor_150=0
p_olhos_azuis=0
p_olhos_pretos=0
p_olhos_castanho=0
p_olhos_verdes=0
p_ruiva_s_olhos_azuis=0
p_50anos_60kg=0
idade_p_menor_150=0

while x<3:

    idade=int(input('Digite sua idade:\n'))
    peso=int(input('Digite seu peso:\n'))
    if idade>50 and peso<60:
        p_50anos_60kg+=1
        
    altura=int(input ('Digite sua altura em centímetros:\n'))
    if altura<150:
        p_alt_menor_150+=1
        idade_p_menor_150+=idade
    olhos=(input('Qual é a cor dos seus olhos:\n [A] Azul\n [P] Preto\n [V] Verde\n [C] Castanho\n'))
    if olhos=='c':
        p_olhos_castanho+=1
    elif olhos=='a':
        p_olhos_azuis+=1
    elif olhos=='v':
        p_olhos_verdes+=1
    elif olhos=='p':
        p_olhos_pretos+=1
    cabelo=(input('Qual é a cor dos seus cabelos:\n [P] Preto\n [C] Castanho\n [L] Louro\n [R] Ruivo\n'))
    if cabelo == 'r' and olhos!='a':
        p_ruiva_s_olhos_azuis+=1
    x=x+1
print(f'O número de pessoas com idade superior a 50 anos e com peso inferior a 60 anos é {p_50anos_60kg}.'
    f'A média de idade das pessoas que medem menos que 1,50 é {(idade_p_menor_150/p_alt_menor_150)} anos.'
    f'A porcentagem de pessoas ruivas que não possuem olhos azuis é {(p_ruiva_s_olhos_azuis*100/25)}%.')

