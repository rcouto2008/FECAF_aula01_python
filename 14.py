# 14 Elabore um programa que calcule e apresente o volume de uma caixa retangular, por meio da fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.

comp = float(input("digite o comprimeto "))
larg = float(input("digite a largura "))
alt = float(input("digite a altura "))

volume = comp * larg * alt
msg = f" a caixa possui {volume} L"
print(msg)
