from meus_projetos.Funcoes_Cadastro import *
from time import sleep

listaPaciente = []
print("\033[1;30;47m PACIENTE \033[m")
informacoesPaciente(listaPaciente)
linha(listaPaciente)

print("\033[1;30;47m Exibindo Dados do Pacientes... \033[m")
sleep(1)
linha(listaPaciente)
exibirPacientes(listaPaciente)


print("\033[1;30;47m Verificando Suspeita de Doença Contagiosa... \033[m")
sleep(2)
print(verificandoDoenca(listaPaciente))

print("\033[1;30;47m Verificando prioridade do paciente... \033[m")
sleep(2)
linha(listaPaciente)
verificaIdade(listaPaciente)
