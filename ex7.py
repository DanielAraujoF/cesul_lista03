# 7) Uma loja deseja calcular o preço final a ser cobrado por uma duplicata.
# Esta loja aplica uma multa de 5% do valor da duplicata para cada dia de atraso.

valorDuplicata = float(input("Valor da duplicata: "))
diasDeAtraso = int(input("Dias de atraso após prazo limite: "))
multa = 5

valorTotal = valorDuplicata + ((multa / 100) * diasDeAtraso) * valorDuplicata

print(f"O valor da duplicata somado ao valor é R${valorTotal:.2f}")