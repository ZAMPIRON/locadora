# Sistema de Locadora em Python 🎬

Este projeto é um **sistema de locadora de filmes e jogos** desenvolvido em Python.  
Ele permite o **cadastro de clientes e itens**, além de **controle de empréstimos** (locação e devolução de filmes e jogos).  

---

## Funcionalidades
- **Menu Locadora**
  - Cadastrar clientes
  - Cadastrar itens (Filmes ou Jogos)
  - Listar todos os clientes
  - Listar todos os itens disponíveis ou alugados

- **Menu Cliente**
  - Listar itens já locados
  - Locar um item (se disponível)
  - Devolver um item

- **Validações**
  - Impede locação de item já alugado
  - Impede devolução de item que o cliente não possui
  - Verificação caso não exista cliente ou item cadastrado

---

## Estrutura do Projeto 🛠️ 
O projeto está dividido em **dois arquivos principais**:

---

## Classes 📚

### 🔹 `Item`
Classe base para representar filmes e jogos.  
Atributos principais:
- `id` → Identificação do item  
- `titulo` → Nome do filme/jogo  
- `disp` → Disponibilidade (True = disponível, False = alugado)  

Métodos:
- `alugar()` → Marca item como alugado  
- `devolver()` → Marca item como disponível  

---

### 🔹 `Filme (Item)`
Herdada de `Item`.  
Atributos extras: `gênero` e `duração`.

---

### 🔹 `Jogo (Item)`
Herdada de `Item`.  
Atributos extras: `plataforma` e `faixa etária`.

---

### 🔹 `Cliente`
Representa um cliente da locadora.  
Atributos: `nome`, `cpf` e `itens_locados`.  
Métodos:
- `locar(item)`  
- `devolver(item)`  
- `listarLocados()`  

---

### 🔹 `Locadora`
Gerencia todos os **clientes e itens**.  
Métodos:
- `cadastroCliente(cliente)`  
- `cadastroItem(item)`  
- `listarClientes()`  
- `listarItens()`  
- `buscarCliente(cpf)`  
- `buscarItem(id)`  

---
