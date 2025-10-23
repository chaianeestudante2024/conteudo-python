
#Pergunta para o usuário:
# Sobre o preço de três produtos:


preco_1 = float(input("Digite o preço do primeiro produto: "))
preco_2 = float(input("Digite o preço do segundo produto: "))
preco_3 = float(input("Digite o preço do terceiro produto: "))

if preco_1 < preco_2 and preco_1 < preco_3:
    print("Você deveria comprar o produto que custa",preco_1,"R$")
elif preco_2 < preco_1 and preco_2 < preco_3:
    print("Você deveria comprar o produto que custa",preco_2,"R$")
elif preco_3 < preco_1 and preco_3 < preco_2:
    print("Você deveria comprar o produto que custa",preco_3,"R$")
else:
    print("Os preços são iguais")
    print("Pode comprar qualquer um")