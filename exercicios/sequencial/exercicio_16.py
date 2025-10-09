# Programa para loja de tintas:

metros_pintados = float(input("Qual é o tamanho em metros quadrados que deseja pintar? "))

quantidade_tinta =  metros_pintados / 3

quantidade_lata = quantidade_tinta / 18
print("A quantidade de latas necessárias será ",quantidade_lata)

preco_lata = 80
preco_total = quantidade_lata * preco_lata
print("O preço total á ser pago é de",preco_total,"R$")


