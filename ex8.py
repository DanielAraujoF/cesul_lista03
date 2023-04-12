# 8) Escreva um programa que determine o número de dias e de horas que uma pessoa já viveu.
# Considere que um mês tem 30 dias.

idadeUser = int(input("Olá, este programa calcula quantos dias e quantas horas você já viveu até o primeiro dia do ano. Qual sua idade:"))

diasVividos = idadeUser * 365
#porque tem 365 dias no ano
horasVividas = diasVividos * 24
#porque tem 24h num dia

print(f"Você já viveu {diasVividos:.2f} dias, e o número de horas que você já viveu é de {horasVividas:.2f}")