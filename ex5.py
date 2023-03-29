# 5) Um mestre de obras quer calcular quanto de argamassa e rejunte serão precisos para trocar o piso de uma casa.
# Desenvolva um programa que receba do usuário a área total da casa (em m2 ) e calcule como saída:
# • Quantos Kg de rejunte serão utilizados para aplicação (considerar 1Kg para 3m2 )
# • Quantos Kg de argamassa serão utilizados para a aplicação (considerar 1kg por 5m2 )

area = float(input("Insira a area da sala: "))

qtdDeRejunte = area / 3
qtdDeArgamassa = area / 5

print("A quantidade de rejunte e argamassa a serem utilizados é, respectivamente:", qtdDeRejunte, "e", qtdDeArgamassa)
