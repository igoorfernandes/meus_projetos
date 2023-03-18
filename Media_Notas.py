from time import sleep
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

print("Calculando sua média...")
sleep(1)
print("Sua nota foi: ", media)

if media >= 6:
    print("\033[1;33mParabéns você Passou!!!\033[m")

elif media > 4:
    print("\033[1;34mPrecisa estudar mais, você esta de recuperação\033[m.")

else:
    print("\033[1;31mQue pena, você não Passou!!!\033[m")

