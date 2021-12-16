nome = input("Digite o nome: ");
idade = int(input("Digite a idade: "));
doencaInfectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper();

#enquanto o usuário digitar uma resposta diferente das opções, a msg continuara aparecendo
while (doencaInfectocontagiosa != "SIM" and doencaInfectocontagiosa != "NAO"):
    print("Digite SIM ou NAO");

#Após a resposta, aparecerá a pergunta que desencandeará um outro evento    
    doencaInfectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper();

#Definição da sala que o paciente irá
if (doencaInfectocontagiosa=="SIM"):
    print("Encaminhe o paciente para sala AMARELA");
else:
    print("Encaminhe o paciente para sala BRANCA");

#Caso o usuário seja maior de 65, ele terá atendimento prioritário automaticamente,  
#caso contrário, será perguntado seu genêro para ver se ele também necessita de prioridade
if (idade >= 65):
    print("Paciente COM prioridade");
else:
    genero=input("Digite o gênero do paciente: ").upper();
#Caso a usuária seja feminino, será verificado se está gravida, **caso seja masculino, ele já não terá prioridade
    if (genero=="FEMININO" and idade > 10):
        gravidez = input("A paciente está grávida? ").upper();
        if (gravidez == "SIM"):
            print("Paciente COM prioridade");
        else:
            print("Paciente SEM prioridade");
    else:
        print("Paciente SEM prioridade");