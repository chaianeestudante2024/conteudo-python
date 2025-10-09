# Calculo para rendimento do pescador:

peixe_peso = float(input("Quantidade de peixe:"))
limite = 50


excesso = limite - peixe_peso
print("O excesso é de",excesso,"Kg")
multa = 4 * excesso
print("A multa é de",multa,"R$")
