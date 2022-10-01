n_macos= float(input("Digite o número de maços de cigarro consumidos diáriamente: "))
tempo= int(input("Há quanto tempo (em dias) você fuma? "))

perda_diaria= (n_macos * 3.4)/24
perda_total=perda_diaria * tempo
print(f"Voce perdeu {perda_total:.2f} dias da sua vida!")

if tempo <= 90:
  print(f"Você é um fumante ocasional e seus dentes começam a amarelar")
elif tempo > 90 and tempo <= 365:
  print(f"Você é um fumante habitual e seu paladar já não é o mesmo e sua respiração nem se fala. Ainda da tempo de parar!")
else:
  print(f"Você é um fumante ativo e seu pulmão está realmente comprometido. PARE AGORA!")
