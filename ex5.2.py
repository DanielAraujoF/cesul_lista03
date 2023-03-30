# 5) Um mestre de obras quer calcular quanto de argamassa e rejunte serão precisos para trocar o piso de uma casa.
# Desenvolva um programa que receba do usuário a área total da casa (em m2 ) e calcule como saída:
# • Quantos Kg de rejunte serão utilizados para aplicação (considerar 1Kg para 3m2 )
# • Quantos Kg de argamassa serão utilizados para a aplicação (considerar 1kg por 5m2 )

area = float(input("Insira a area da sala: "))

qtdDeRejunte = area / 3
qtdDeArgamassa = area / 5

# caso você coloque o número 100 no input, o número do rejunte vai resultar em 33,333333336.
# Para erradicar esse problema, colocar -- :.1f -- depois da variável desejada.
msgRejunte = f"A quantidade de rejunte a ser usado é {qtdDeRejunte}kg. "
print(msgRejunte)
# ou -- print(msgRejunte.format(qtdDeRejunte, qtdDeArgamassa)) --
# mas sem o "f" na frente da string

# pode ser feito da seguinte forma também:
print(f"A quantidade de argamassa a ser utilizada é {qtdDeArgamassa}kg.")
