from Meus_Projetos.Funcoes_Cadastro import *
from time import  sleep

resp = "SIM"
while resp == "SIM":
    linhas = []

    linha(linhas)
    taboada = int(input("Digite um Número: "))
    linha(linhas)
    print("Calculando...")
    sleep(2)
    linha(linhas)
    for valor in range(1,11,1):
        valores = valor * taboada
        print(taboada, "X", valor, "=", valores)
    resp = input("Deseja continuar? ").upper()
    linha(linhas)
print("FIM")
linha(linhas)