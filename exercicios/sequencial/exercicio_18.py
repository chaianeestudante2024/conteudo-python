# Programa de tempo de download:
# O tamanho do arquivo deverá ser em MB
# A unidade de velocidade deverá ser convertida de Mbps para MB/min

print("Responda a pergunta para saber o tempo de download do seu arquivo: ")
print()

# Pergunta que será feita para o usuário:
tamanho_arquivo = float(input("Qual é o tamanho do seu arquivo? "))
velocidade_Internet = float(input("Qual é a velocidade do link de internet? "))

# Aqui é feito a conversão de Mbps para MB/s
conversao_mbps_mb = velocidade_Internet / 8

# Cálculo do tempo de download em MB/s =
tempo_MBS = tamanho_arquivo / conversao_mbps_mb

# Aqui acontece a conversão de MB/s para MB/min:
conversao_MBM = tempo_MBS * 60

#Aqui mostra o tempo de download do arquivo para o usuário:
print("O tempo de download do seu arquivo é de",conversao_MBM,"MB/min")


