
#Pergunta para o usuário sobre os números:

numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
numero3 = float(input("Digite o terceiro valor: "))

#Lógica de se o número for maior:

if numero1 > numero2 and numero1 > numero3:
    print("O primeiro valor",numero1,"é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo valor",numero2,"é o maior")
elif numero3 > numero1 and numero3 > numero2:
    print("O terceiro valor",numero3,"é o maior")
else:
    print("Os números são iguais")

#Lógica de se o número for menor:

if numero1 < numero2 and numero1 < numero3:
    print("O primeiro valor ",numero1,"é o menor")
elif numero2 < numero1 and numero2 < numero3:
    print("O segundo valor",numero2,"é o menor")
elif numero3 < numero1 and numero3 < numero2:
    print("O terceiro valor",numero3,"é o menor")
else:
    print("Os números são iguais")