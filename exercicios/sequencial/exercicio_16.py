# Programa para loja de tintas:
# Pergunta que será feita para o usuário:

import math

metros_pintados = float(input("Qual é o tamanho em metros quadrados que deseja pintar? "))

# Dados de quantidade:

quantidade_tinta =  metros_pintados / 3
print("Serão necessários",quantidade_tinta,"L")

quantidade_lata = math.ceil(quantidade_tinta / 18)

#Aqui mostrará a quantidade de latas á ser comprada:
print("A quantidade de latas necessárias será ",quantidade_lata)

# Dados de preço:

preco_lata = 80
preco_total = quantidade_lata * preco_lata

# Aqui mostrará o valor total:
print("O preço total á ser pago é de","R$",round(preco_total,2))



