tempo=float(input('Quantas horas vão durar a viagem?\n'))
km= float(input('Qual vai ser velocidade média?:\n'))
distancia=tempo * km
litros= distancia/2
print(f' Para essa viagem serão necessários {litros} litro de gasolina.')
