#Venda de combustiveís pelo um posto:

print("A-Álcool | G- Gasolina")
preco_alcool =  4.17
preco_gasolina = 6.29

litros_vendidos = float(input("Insira a quantidade de litros vendidos: "))
tipo_combustivel = input("Insira o tipo de combustivel: ")

if tipo_combustivel == "A" :
    preco_alcool_total = litros_vendidos * preco_alcool
    print("O preço original era de R$",preco_alcool_total)
if tipo_combustivel == "A" and litros_vendidos <= 20:
    desconto_alcool_20 = (litros_vendidos * preco_alcool) - (litros_vendidos * preco_alcool * 0.03)
    print("O preço com 3% desconto é de",desconto_alcool_20)
elif tipo_combustivel == "A" and litros_vendidos > 20:
    desconto_alcool_acima_20 = (litros_vendidos * preco_alcool) - (litros_vendidos * preco_alcool * 0.05)
    print("O preço com 5% desconto é de",desconto_alcool_acima_20)


if tipo_combustivel == "G" :
    preco_gasolina_total = litros_vendidos * preco_gasolina
    print("O preço original era de R$",preco_gasolina_total)
if tipo_combustivel == "G" and litros_vendidos <= 20:
    desconto_gasolina_20 = (litros_vendidos * preco_gasolina) - (litros_vendidos  * preco_gasolina * 0.04)
    print("O preço com 4% desconto é de",desconto_gasolina_20)
elif tipo_combustivel == "G" and litros_vendidos > 20:
    desconto_gasolina_acima_20 = (litros_vendidos * preco_gasolina) - (litros_vendidos * preco_gasolina * 0.06)
    print("O preço com 6% desconto é de",desconto_gasolina_acima_20)

