#  10 Calcule e apresente o valor do volume de uma lata de óleo, utilizando a fórmula: volume = π * raio ** 2 * altura. Considere o valor de π como 3.1415.

altura = int(input("digite a altura da lata "))
raio = float(input("Informe o raio da circunferência da lata"))
π = 3.1415

volume = π * raio ** 2 * altura

rs = volume
msg = f" o volume da lata é de {rs} ml"

print(msg)
