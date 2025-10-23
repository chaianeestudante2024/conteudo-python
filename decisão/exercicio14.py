
#Programa que lê duas notas de um aluno:

nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))

print("Nota 1:",nota_1,"Nota 2:",nota_2)

media = (nota_1 + nota_2) /2
print("Media:",media)

#Conceito A:
if media >=9 or media <= 10:
    print("Aprovado")
    print("CONCEITO A")

#Conceito B:
elif media >=7.5 or media <=9:
    print("Aprovado")
    print("CONCEITO B")

#Conceito C:
elif media >=6 or media <=7.5:
    print("Aprovado")
    print("CONCEITO c")

#Conceito D:
elif media >=4 or media <=6:
    print("Reprovado")
    print("CONCEITO D")
#Conceito E:
elif media >=4 or media <=0:
    print("Reprovado")
    print("CONCEITO E")
