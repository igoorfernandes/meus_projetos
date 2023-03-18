def informacoesPaciente(pacientes):
    paciente = []
    resp = "SIM"
    while resp == "SIM":
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        genero = input("Digite o genero do paciente: ").upper()
        doenca = input("Suespeita de doença contagiosa: ").upper()
        pacientes.append([nome, idade, genero, doenca])
        while doenca != "SIM" and doenca != "NAO":
            print("Digite 'SIM' ou 'NAO'.")
            doenca = input("Suspeita de doença contagiosa: ").upper()
        resp = input("Deseja informa outro paciente? ")





def linha(pacientes):
    print("\033[1;33m = \033[m" * 30)


def exibirPacientes(pacientes):
    for item in pacientes:
        print("Paciente: ", item[0])
        print("Idade: ", item[1])
        print("Genero: ", item[2])
        print("Doença contagiosa: ", item[3])
        print("\033[1;33m = \033[m" * 30)




def verificandoDoenca(pacientes):
    for item in pacientes:
        if item[3] == "SIM":
            print("Encaminhe paciente para sala \033[1;33;40m AMARELA! \033[m")
        else:
            print("Encaminhe o paciente para sala \033[1;;40m BRANCA! \033[m")
    return "\033[1;33m = \033[m" * 30


def verificaIdade(pacientes):
    for item in pacientes:
        gravidez = "NAO"
        if item[1] >= 65:
            print("Paciente COM prioridade de atendimento.")
        else:
            if item[2] == "FEMININO" and item[1] >10:
                gravidez = input("Paciente esta Gravida: ").upper()
                if gravidez == "SIM":
                    print("Paciente ", item[0], " COM prioridade ")
                else:
                    print("Paceinte", item[0], " SEM prioridade ")
            else:
                print("paciente", item[0], " SEM prioridade")