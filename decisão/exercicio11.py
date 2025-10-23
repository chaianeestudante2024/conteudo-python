#Organizações Tabajara:
# Reajustes de um salário de um colaborador:

salario_colaborador = float(input("Insira seu salário: "))

#Reajustes:
if salario_colaborador <= 1450:
    reajuste_20 = salario_colaborador * 0.20
    resultado_20 = reajuste_20 + salario_colaborador
    print("O seu salario antes do reajuste era de", salario_colaborador, "R$")
    print("O percentual de aumento aplicado é de 20%")
    print("O valor do aumento é de", reajuste_20, "R$")
    print("O Novo salário é de", resultado_20, "R$")

elif salario_colaborador >= 1451  or salario_colaborador  <= 2800:
    reajuste_15 = salario_colaborador * 0.15
    resultado_15 = salario_colaborador + reajuste_15
#Informar na tela:
    print("O seu salario antes do reajuste era de",salario_colaborador,"R$")
    print("O percentual de aumento aplicado é de 15%")
    print("O valor do aumento é de",reajuste_15,"R$")
    print("O Novo salário é de",resultado_15,"R$")

elif salario_colaborador >= 2800 or salario_colaborador <= 3500:
    reajuste_10 = salario_colaborador * 0.10
    resultado_10 = salario_colaborador + reajuste_10
    print("O seu salario antes do reajuste era de", salario_colaborador, "R$")
    print("O percentual de aumento aplicado é de 10%")
    print("O valor do aumento é de", reajuste_10, "R$")
    print("O Novo salário é de", resultado_10, "R$")

elif salario_colaborador >= 3500:
    reajuste_5 = salario_colaborador * 0.05
    resultado_5 = reajuste_5 + salario_colaborador
    print("O seu salario antes do reajuste era de", salario_colaborador, "R$")
    print("O percentual de aumento aplicado é de 5%")
    print("O valor do aumento é de", reajuste_5, "R$")
    print("O Novo salário é de", resultado_5, "R$")


