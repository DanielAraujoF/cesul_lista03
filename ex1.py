#para realizar o cálculo da área de um círculo

raio = float(input("informe o raio do círculo:"))
#primeiro ele nomeia o input, após isso é traduzido para float (número decimal) =! de int (número natural), depois ele repassa o valor para a variável "raio"

area = 3.14159 * (raio ** 2)

print("a área do círculo é", area)
