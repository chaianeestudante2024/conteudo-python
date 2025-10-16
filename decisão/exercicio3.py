
print(" M - Masculino | F-Femenino | O - outros")
sexo = input("Qual é o seu sexo? ")

if sexo == "F":
    print("Você escolheu a opção Femenino")
elif sexo == "M":
    print("Você escolheu a opção Masculuno")
else:
    print("Você escolheu a opção Outros")

match sexo:
    case "F":
     print("Você escolheu a opção Femenino")
    case "M":
        print("Você escolheu a opção Masculuno")
    case _:
        print("Você escolheu a opção Outros")
