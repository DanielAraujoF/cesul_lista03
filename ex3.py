# 3) Escreva um algoritmo que leia uma temperatura em graus Celsius e a converta para graus Fahrenheit.
# Fórmula de conversão: F = C * 1.8 + 32

tempC = float(input("Para converter a temperatura atual para Fahrenheit informe a temperatura atual (em celsius): "))

tempF = (tempC * 1.8) + 32

print("A temperatura atual em Fahrenheit é:", tempF)
