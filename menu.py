import os
from classes import *
from funcoes import *
clientes = []
itens = []
def menu_cliente():
    print("\n\tOpções\n1 - Listar itens locados \n2 - Locar item \n3 - Devolver item")
    opcao = int(input("--> "))
    match opcao:
        case 1:
            Cliente.listarLocados()
        case 2:
            Cliente.locar()
        case 3:
            Cliente.devolver()
        case _:
            print("SAINDO...")
            os.system("pause")

def menuLocadora():
    print("\n\tOpcoes\n1 - Cadastrar Cliente \n2 - Cadastrar Item \n3 - Listar Clientes \n4 - Listar Itens")
    opcao = int(input("--> "))
    match opcao:
        case 1:
            Locadora.cadastroCliente(cliente= Cliente)
        case 2:
            Locadora.cadastroItem(item= Item)
        case 3:
            Locadora.listarClientes(cliente= Cliente)
        case 4:
            Locadora.listarItens(item= Item)
        case _:
            print("SAINDO...")
            os.system("pause")
while True:
    print("\n\tBEM VINDO AO MENU\n")
    print("1 - Cliente\n2 - Locadora")
    try:
        escolha = int(input("\nSELECIONE: "))
    except Exception:
        print("Digite um número válido!")
        os.system("pause")

    match escolha: 
        case 1:
            cliente_nome = input("Olá, qual é seu nome? ")
            print(f"Seja bem vindo, {cliente_nome.capitalize}")
            clientes.append(cliente_nome)
            menu_cliente()
        case 2: 
            senha = 1234
            senha_locadora = int(input("Digite a senha: "))
            match senha_locadora:
                case 1234:
                    print("Seja bem vindo!")
                    menuLocadora()
