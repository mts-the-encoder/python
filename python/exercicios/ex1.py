from typing import MappingView


nivel = input("Informe seu nível de acesso: ").upper();
genero = input("Seu gênero: ").upper();

if (nivel == "ADM" and genero == "FEMININO"):
    print("Olá administradora");
elif (nivel == "ADM" and genero == "MASCULINO"):
    print("Olá administrador");
elif (nivel == "USR" and genero == "FEMININO"):
    print("Olá usuária");
elif (nivel == "USR" and genero == "MASCULINO"):
    print("Olá usuário")
elif (nivel == "GUEST"):
    print("Olá visitante");
else: 
    print("Olá desconhecido(a)");
    