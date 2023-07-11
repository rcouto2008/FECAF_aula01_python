# 15 Elabore um programa de computador que efetue a leitura de quatro valores inteiros (variáveis A, B, C e D). Ao final, o programa deve apresentar o
# resultado do produto (variável P) do primeiro com o terceiro valor, e o resultado do produto (variável P) do primeiro com o terceiro valor, e o resultado
# da soma (variável S) do segundo com o quarto valor.

a = int(input("digite o valor de A "))
b = int(input("digite o valor de B "))
c = int(input("digite o valor de C "))
d = int(input("digite o valor de D "))

var_p = a * c
var_s = b + d 
msg = f"o valor de A para C é {var_p} e o valor da soma de B para D é {var_s}"
print(msg)
