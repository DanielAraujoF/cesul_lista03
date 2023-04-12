# 7) Uma loja deseja calcular o preço final a ser cobrado por uma duplicata.
# Esta loja aplica uma multa de 5% do valor da duplicata para cada dia de atraso.

valorDuplicata = float(input("Valor da duplicata: "))
diasDeAtraso = int(input("Dias de atraso após prazo limite: "))
multa = 5

valorMulta = (multa / 100) * valorDuplicata
totalMulta = valorMulta * diasDeAtraso
total = valorDuplicata + valorMulta

print(f"O valor da duplicata somado ao valor é R${total:.2f}")

# converter o tipo da entrada (ex: de string para float) chama se TYPE CASTING