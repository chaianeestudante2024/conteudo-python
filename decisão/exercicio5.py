
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2
print("Sua média é ",media)

if media >= 7:
    print("Aprovado 😊")
elif media < 7:
    print("Reprovado 😵")
elif media == 10:
    print("Aluno Destaque 😎")