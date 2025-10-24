#Programa de Triãngulos:

triangulo_lado_1 = int(input("Informe o primeiro lado do triângulo: "))
triangulo_lado_2 = int(input("Informe o segundo lado do triângulo: "))
triangulo_lado_3 = int(input("Informe o terceiro lado do triângulo: "))

if triangulo_lado_1 + triangulo_lado_2 > triangulo_lado_3:
    print("É um triângulo")
elif triangulo_lado_2 + triangulo_lado_3 > triangulo_lado_1:
    print("É um triângulo")
elif triangulo_lado_2 + triangulo_lado_1 > triangulo_lado_3:
    print("É um triângulo")
elif triangulo_lado_1 + triangulo_lado_3 > triangulo_lado_2:
    print("É um triângulo")
else:
    print("Não é um triângulo")
    exit(1)
#Tipo do Triãngulo:
#Equilatero:
if triangulo_lado_1 == triangulo_lado_2 == triangulo_lado_3:
    print("É um triângulo equilatero")
#Isoceles:
elif triangulo_lado_1 == triangulo_lado_2 != triangulo_lado_3:
    print("É um triângulo isósceles")
elif triangulo_lado_1 == triangulo_lado_3 != triangulo_lado_2:
    print("É um triângulo isósceles")
elif triangulo_lado_2 == triangulo_lado_3 != triangulo_lado_1:
    print("É um triângulo isósceles")
#Triângulo Escaleno:
else:
    print("Os lados são diferentes")

