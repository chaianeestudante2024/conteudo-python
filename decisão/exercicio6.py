
#Pergunta para o usuário sobre os números:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

#Lógica:
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número",numero1,"é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo número",numero2,"é o maior")
elif numero3 > numero1 and numero3 > numero1:
    print("O terceiro número",numero3,"é o maior")
else:
    print("Os números são iguais")

