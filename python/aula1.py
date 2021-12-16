#Criando variáveis com vários tipos e inputs (String, float e int)
nome = input("Digite um funcionário: ");
empresa = input("Digite a instituição: ");
qtdFuncionarios = int(input("Digite a qtde de funcionários: ")); #Int... um valor inteiro
mediaMensalidade = float(input("Digite a média da mensalidade: "));  #Float... um valor decimal
#Aqui será exibido as variáveis unidas em uma única string
print(nome + " trabalha na empresa " + empresa);
print("Possui: ", qtdFuncionarios, " funcionarios.");
print("A média da mensalidade é de: " + str(mediaMensalidade));
print("============== Verifique os tipos de dados abaixo: ==============");
#Exibindo o tipo das variáveis
print("O tipo de dado da variavel [nome] é: ",type(nome));
print("O tipo de dado da variavel [empresa] é: ",type(empresa));
print("O tipo de dado da variavel [qtdFuncionarios] é: ",type(qtdFuncionarios));
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade));