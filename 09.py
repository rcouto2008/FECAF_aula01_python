# 09 Leia o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o valor do percentual de reajuste (variável PR) a ser atribuído.
# Apresente o valor do novo salário (variável NS).

sm = float(input(" DIGITE SEU SALÁRO"))
pr = float(input("DIGITE O VALOR DO PERCENTUAL DO REAJUSTE "))

ns = pr / 100 * sm

resultado = ns + sm
msg = f" seu sário será reajustado no valor de {resultado} reais"
print(msg)
