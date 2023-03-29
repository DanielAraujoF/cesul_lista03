#4) Escreva um algoritmo que leia uma temperatura em graus Fahrenheit e a converta para graus Celsius.
# Fórmula de conversão: C = (F - 32) / 1.8

tempF = float(input("Para converter a temperatura atual para Ceslsius informe a temperatura atual (em Fahrenheit): "))

tempC = (tempF - 32) / 1.8

print("A temperatura atual em Celsius é:", tempC)
