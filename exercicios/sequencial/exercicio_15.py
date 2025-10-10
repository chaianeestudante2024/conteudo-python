#Salário:

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou? "))

# Aqui mostrára o salário sem nenhum desconto:
salario_bruto = ganho_hora * horas_trabalhadas
print("O seu salário bruto é de",salario_bruto)

# Descontos:

imposto_renda = salario_bruto * 0.11
print("O valor do imposto de renda foi",imposto_renda,"R$")

inss = salario_bruto * 0.08
print("Foi pago ao INSS",inss,"R$")

sindicato = salario_bruto * 0.05
print("Foi pago ao Sindicato",sindicato,"R$")

# Aqui mostrará o salário com todos os descontos:
salario_liquido = salario_bruto - ( imposto_renda + inss + sindicato )
print("O seu salário liquido é de",salario_liquido,"R$")










