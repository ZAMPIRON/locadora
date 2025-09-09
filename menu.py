import os
from classes import *

locadora = Locadora()

def menu_cliente():
    if not locadora._Locadora__clientes:  
        print("Nenhum cliente cadastrado ainda. Peça para a locadora cadastrar primeiro!")
        return
    cpf = input("Digite o CPF do cliente: ")
    cliente = locadora.buscarCliente(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    print(f"Seja bem-vindo, {cliente.getNome()}!")

    while True:
        print("\n\t=== Menu Cliente ===")
        print("1 - Listar itens locados")
        print("2 - Locar item")
        print("3 - Devolver item")
        print("0 - Voltar")
        try:
            opcao = int(input("--> "))
        except ValueError:
            print("Digite um número válido!")
            os.system("pause")
            continue

        match opcao:
            case 1:
                cliente.listarLocados()
            case 2:
                locadora.listarItens()
                try:
                    id_item = int(input("Digite o ID do item: "))
                    item = locadora.buscarItem(id_item)
                    if item:
                        cliente.locar(item)
                    else:
                        print("Item não encontrado.")
                except ValueError:
                    print("ID inválido.")
            case 3:
                cliente.listarLocados()
                try:
                    id_item = int(input("Digite o ID do item para devolver: "))
                    item = locadora.buscarItem(id_item)
                    if item:
                        cliente.devolver(item)
                    else:
                        print("Item não encontrado.")
                except ValueError:
                    print("ID inválido.")
            case 0:
                break
            case _:
                print("Opção inválida.")


def menuLocadora():
    while True:
        print("\n\t=== Menu Locadora ===")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Item")
        print("3 - Listar Clientes")
        print("4 - Listar Itens")
        print("0 - Voltar")
        try:
            opcao = int(input("--> "))
        except ValueError:
            print("Digite um número válido!")
            os.system("pause")
            continue

        match opcao:
            case 1:
                nome = input("Nome do cliente: ")
                cpf = input("CPF do cliente: ")
                locadora.cadastroCliente(Cliente(nome, cpf))
            case 2:
                tipo = input("Digite F para Filme ou J para Jogo: ").upper()
                id_item = int(input("ID: "))
                titulo = input("Título: ")
                if tipo == "F":
                    genero = input("Gênero: ")
                    duracao = int(input("Duração (min): "))
                    locadora.cadastroItem(Filme(id_item, titulo, genero, duracao))
                elif tipo == "J":
                    plataforma = input("Plataforma: ")
                    faixa = input("Faixa etária: ")
                    locadora.cadastroItem(Jogo(id_item, titulo, plataforma, faixa))
                else:
                    print("Tipo inválido.")
            case 3:
                locadora.listarClientes()
            case 4:
                locadora.listarItens()
            case 0:
                break
            case _:
                print("Opção inválida.")


while True:
    print("\n\t=== MENU PRINCIPAL ===\n")
    print("1 - Cliente")
    print("2 - Locadora")
    print("0 - Sair")
    try:
        escolha = int(input("\nSELECIONE: "))
    except ValueError:
        print("Digite um número válido!")
        os.system("pause")
        continue

    match escolha: 
        case 1:            
            menu_cliente()
        case 2: 
            senha_locadora = int(input("Digite a senha da locadora: "))
            if senha_locadora == 1234:
                print("Seja bem-vindo à Locadora!")
                menuLocadora()
            else:
                print("Senha incorreta!")
        case 0:
            print("Encerrando o sistema...")
            break
        case _:
            print("Opção inválida.")
