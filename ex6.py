# 6) Escreva um programa que calcule o preço final de uma venda, a partir do preço unitário do produto, a quantidade vendida e o percentual de desconto

# precoUn == preço unitário
# qntVend == quantidade vendida
# percentDesc == desconto em porcentagem a ser aplicado

precoUn = float(input("Bom dia! Insira o valor unitário, sem o desconto, do produto desejado: "))
qntVend = int(input("Agora, por favor, informe a quantia vendida do produto desejado: "))
percentDesc = float(input("Por fim, indique qual o percentual de desconto é dado ao produto: "))

totalSemDesc = precoUn * qntVend
print(f"O valor total da quantia inserida, sem o desconto é: {totalSemDesc:.2f}")

valorDesc = totalSemDesc * (percentDesc / 100)
print(f"O valor descontado do valor total: {valorDesc:.2f}")

totalComDesc = (precoUn * qntVend) * (percentDesc / 100)
print(f"Já o valor total da quantia, com o desconto é: {totalComDesc:.2f}")
