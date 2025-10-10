# Calculo para rendimento do pescador:
# Dados que vão ser colocados pelo pescador:

peixe_peso = float(input("Quantidade de peixe:"))

limite = 50
multa_por_kg = 4

if peixe_peso > limite:

# Conta de excesso e multa:

    excesso =  peixe_peso - limite
    print("O excesso é de",excesso,"Kg")
    multa = multa_por_kg * excesso
    print("A multa é de",multa,"R$")
else:
    print("Não foi maior do que o permitido")
print("Fora da identação")

