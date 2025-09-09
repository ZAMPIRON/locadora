class Item:
    def __init__(self, id, titulo): 
        self.__id = id
        self.__titulo = titulo
        self.__disp = True

    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo
    
    def getDisp(self):
        return self.__disp
    
    def alugar(self):
        if self.__disp:
            self.__disp = False
            return f"{self.__titulo} foi alugado com sucesso"
        else:
            return f"{self.__titulo} já está alugado"
    
    def devolver(self):
        self.__disp = True
        return f"{self.__titulo} foi devolvido e está disponível novamente."


class Filme(Item):
    def __init__(self, id, titulo, genero, duracao):
        super().__init__(id, titulo)
        self.__genero = genero
        self.__duracao = duracao
    

class Jogo(Item):
    def __init__(self, id, titulo, plataforma, faixa):
        super().__init__(id, titulo)
        self.__plataforma = plataforma
        self.__faixa = faixa
    

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = []
    
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def locar(self, item: Item):
        if item.getDisp():
            print(item.alugar())
            self.__itens_locados.append(item)
        else:
            print("Item indisponível.")
    
    def devolver(self, item: Item):
        if item in self.__itens_locados:
            print(item.devolver())
            self.__itens_locados.remove(item)
        else:
            print("Esse item não está com você.")
    
    def listarLocados(self):
        if not self.__itens_locados:
            print("Nenhum item locado.")
        else:
            print("Itens locados:")
            for i in self.__itens_locados:
                print("-", i.getTitulo())


class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    def cadastroCliente(self, cliente: Cliente):
        self.__clientes.append(cliente)
        print(f"Cliente {cliente.getNome()} cadastrado.")

    def cadastroItem(self, item: Item):
        self.__itens.append(item)
        print(f"Item {item.getTitulo()} cadastrado.")

    def listarClientes(self):
        if not self.__clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in self.__clientes:
                print(f"Nome: {c.getNome()} - CPF: {c.getCpf()}")

    def listarItens(self):
        if not self.__itens:
            print("Nenhum item cadastrado.")
        else:
            for i in self.__itens:
                status = "Disponível" if i.getDisp() else "Alugado"
                print(f"ID: {i.getId()} - {i.getTitulo()} - {status}")

    def buscarCliente(self, cpf):
        for c in self.__clientes:
            if c.getCpf() == cpf:
                return c
        return None

    def buscarItem(self, id):
        for i in self.__itens:
            if i.getId() == id:
                return i
        return None
