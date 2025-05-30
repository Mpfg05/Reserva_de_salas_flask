## 🏫 API de Reserva de Salas

## 📝 Descrição da API
Este repositório contém a API de Reserva de Salas, responsável por gerenciar as reservas de salas de aula. A API permite criar, listar e gerenciar reservas, garantindo que não haja conflitos de horários e salas. Ela integra-se com o microserviço de Sistema de Gerenciamento para obter informações sobre turmas e professores.
Validações feitas via requisição externa:

---


## 🐳 Instruções de Execução (com Docker)

1. Clone o repositório:
   
```bash
git clone https://github.com/Mpfg05/Reserva_de_salas_flask.git
cd Reserva_de_salas_flask
```

2. Build manual da imagem Docker

```bash
docker build -t reserva-salas .
```

3. Execute o container:

```bash
docker run -d -p 5000:5000 reserva-salas
```

4. A API estará disponível em:
http://localhost:5000


---


## 🏗️ Explicação da Arquitetura Utilizada

* Framework:
Utiliza o Flask, um microframework em Python, para desenvolvimento da API RESTful.

* Banco de Dados:
Utiliza SQLite para persistência dos dados de reservas.

* Integração com Sistema de Gerenciamento:
A API consome endpoints do microserviço de Sistema de Gerenciamento para validar e obter informações sobre turmas e professores.

* Validações:
Implementa validações para evitar conflitos de reservas, garantindo que uma sala não seja reservada por mais de uma turma no mesmo horário.

* Docker:
A aplicação é containerizada utilizando Docker, facilitando o deploy e garantindo a padronização do ambiente de execução.
    
---

## 🌐 Descrição do Ecossistema de Microserviços

Este projeto faz parte de um ecossistema de microserviços integrados, composto por três APIs:

1. Sistema de Gerenciamento:
Responsável por fornecer os dados mestres de alunos, professores e turmas.

2. Reservas (esta API):
Gerencia as reservas de salas de aula, integrando-se com o Sistema de Gerenciamento para obter informações sobre turmas e professores.

3. Atividades:
Microserviço que gerencia o controle de atividades, utilizando o ID do professor disponibilizado pela API do Sistema de Gerenciamento.

A integração entre os microserviços ocorre por meio de troca de dados através das APIs RESTful, permitindo uma arquitetura desacoplada e escalável.


