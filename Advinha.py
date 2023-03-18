from random import randint
from time import sleep

resp1 = 0
resp2 = "SIM"
while resp1 < 5 and resp2 == "SIM":
    # faz o computador "pensar" em um numero de 0 a 5
    computador = randint(0, 5)
    print("\033[1;37m=\033[m" *50)
    print("Vou pensar em um numero de 0 a 5...")
    print("\033[1;37m=\033[m" * 50)
    jogador = int(input("Em que numero eu pensei? "))
    print("\033[1;37m=\033[m" *50)

    print("PROCESSANDO...")
    sleep(2)
    print("\033[1;37m=\033[m" *50)

    if jogador == computador:
        print("\033[0;32mPARABENS!!! voce conseguiu me vencer\033[m")
        resp2 = input("Deseja jogar Novamente? ").upper()
        if resp2 == "SIM":
            resp1 = 0
            continue
        else:
            break
    else:
        print("\033[0;31mGanhei!!! Eu pensei no número ", computador, " e não no ", jogador, "!\033[m")
    resp1 +=1
    if resp1 < 5:
        resp2 = input("Digite <SIM> se deseja tentar novamente. LEMBRANDO que voce só tem mais " + str(5 - resp1) + " Chances. ").upper()

print("FIM DE JOGO!")