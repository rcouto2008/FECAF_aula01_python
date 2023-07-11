# 13 Elabore um programa que efetue a apresentação do valor da conversão em dólar de um valor lido em real. O programa deve solicitar a cotação do dólar e
# também a quantidade de reais disponível com o usuário, para que seja apresentado o valor em moeda americana.

valor_real = float(input("digite o valor em reais R$"))
cotacao_dolar = float(input("cotação do dolar $"))

resultado = valor_real / cotacao_dolar
msg = f" voce possui ${resultado} "
print(msg)
