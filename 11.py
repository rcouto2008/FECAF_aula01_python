#  11 Calcule e apresente o valor de uma prestação em atraso, utilizando a fórmula PRESTACAO = VALOR + (VALOR * TAXA/100) * TEMPO.


vr_prestacao = float(input("Informe o valor da prestação"))
vr_taxa = float(input("informe o valor da taxa de juros "))
tempo = int(input("Informe quantos dias está em atraso"))

prestacao = vr_prestacao + (vr_prestacao * vr_taxa / 100) * tempo

resultado = prestacao

msg = f" o valor da prestação atualizada é de {resultado} reais"
print(msg)
