# Elabore um programa que efetue a apresentação do valor da conversão em real de um valor lido em dólar. O programa deve solicitar o valor da cotação do dólar 
# e também a quantidade de dólares disponível com o usuário, para que seja apresentado o valor em moeda brasileira.

valor_dolar = float(input(" digite o valor em dolar "))
cotacao_real = float(input(" cotação do dolar "))

resultado = valor_dolar * cotacao_real

msg = f" Você tem {resultado} reais "
print(msg)
