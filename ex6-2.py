# 6) Escreva um programa que calcule o preço final de uma venda, a partir do preço unitário do produto, a quantidade vendida e o percentual de desconto

# precoUn == preço unitário
# qntVend == quantidade vendida
# percentDesc == desconto em porcentagem a ser aplicado

precoUn = float(input("Bom dia! Insira o valor unitário do produto vendido: "))
qntVend = int(input("Agora, por favor, informe a quantia vendida do produto desejado: "))
percentDesc = float(input("Por fim, indique qual o percentual de desconto é dado ao produto (Não coloque o sinal de porcentagem '%': "))

totalSemDesc = precoUn * qntVend
print(f"O valor total de {qntVend} unidades vendidas, sem o desconto é R${totalSemDesc:.2f}")

totalComDesc = totalSemDesc * (percentDesc / 100)
print(f"O valor total de {qntVend} vendidas, com o desconto de {percentDesc}% é R${totalComDesc:.2f}")

# Já que não é necessário demonstrar o valor que foi retirado do total sem desconto.