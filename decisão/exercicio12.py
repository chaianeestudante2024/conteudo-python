# Programa para o cálculo de uma folha de pagamento:
#Pergunta para o usuário:


valor_hora = float(input("Insira o valor por hora trabalhada : "))
hora_trabalhada = int(input("Insira a quantidade de horas trabalhadas: "))

#Salário bruto:

salario_bruto = valor_hora * hora_trabalhada
print("Salário Bruto:","(",valor_hora,"*",hora_trabalhada,")",": R$",salario_bruto)

# Desconto Imposto de Renda:

if salario_bruto <=900:
    IR_desconto_900 = 0
    print("IR:", "(", "0%", ")", ": R$", IR_desconto_900)
elif salario_bruto <=1500:
    IR_desconto_1500 = salario_bruto * 0.05
    print("IR:", "(", "5%", ")", ": R$",IR_desconto_1500)
elif salario_bruto <=2500:
    IR_desconto_2500 = salario_bruto * 0.10
    print("IR:", "(", "10%", ")", ": R$",IR_desconto_2500)
elif salario_bruto >=2500:
    IR_desconto_acima_2500 = salario_bruto * 0.20
    print("IR:", "(", "20%", ")", ": R$",IR_desconto_acima_2500)

# Sindicato(desconto):

sindicato_desconto = salario_bruto * 0.03
print("Sindicato:", "(", "3%", ")", ": R$",sindicato_desconto)

#FGTS:
fgts_depositado = salario_bruto * 0.11
print("FGTS:", "(", "11%", ")", ": R$",fgts_depositado)

#Total de descontos:
#Salário Liquido:
if salario_bruto <=900:
    IR_desconto_900 = 0
    total_900 = sindicato_desconto + IR_desconto_900
    print("Total de descontos", ": R$", total_900)
    salario_liquido_900 = salario_bruto - total_900
    print("Salário Liquido", ": R$", salario_liquido_900)

elif salario_bruto <=1500:
    IR_desconto_1500 = salario_bruto * 0.05
    total_1500 = sindicato_desconto + IR_desconto_1500
    print("Total de descontos", ": R$", total_1500)
    salario_liquido_1500 = salario_bruto - total_1500
    print("Salário Liquido", ": R$", salario_liquido_1500)

elif salario_bruto <=2500:
    IR_desconto_2500 = salario_bruto * 0.10
    total_2500 = sindicato_desconto + IR_desconto_2500
    print("Total de descontos",": R$", total_2500)
    salario_liquido_2500 = salario_bruto - total_2500
    print("Salário Liquido", ": R$", salario_liquido_2500)

elif salario_bruto >=2500:
    IR_desconto_acima_2500 = salario_bruto * 0.20
    total_acima_2500 = sindicato_desconto + IR_desconto_acima_2500
    print("Total de descontos", ": R$", total_acima_2500)
    salario_liquido_acima_2500 = salario_bruto - total_acima_2500
    print("Salário Liquido"," : R$", salario_liquido_acima_2500)











