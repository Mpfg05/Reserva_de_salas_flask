## 🏫 API de Reserva de Salas

## 📝 Descrição da API
Microsserviço responsável pela gestão de reservas de salas acadêmicas, integrado ao sistema escolar. Oferece endpoints para criar, listar e remover reservas, com validação externa de turmas.

Validações feitas via requisição externa:

- Verifica se a **turma existe**: `GET /turmas/<id>`
- *(Opcional)* Verifica se o aluno existe: `GET /alunos/<id>`

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- Requests (para integrar com API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/Mpfg05/Reserva_de_salas_flask.git
cd Reserva_de_salas_flask

2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Execute a API
python app.py
A aplicação estará disponível em: http://localhost:5001

📝 O banco de dados SQLite é criado automaticamente na primeira execução.

📡 Endpoints Principais
GET /reservas – Lista todas as reservas

POST /reservas – Cria uma nova reserva

DELETE /reservas/<id> – Remove uma reserva

✅ Exemplo de JSON para criação de reserva:

{
  "turma_id": 1,
  "sala": "204",
  "data": "2025-05-21",
  "hora_inicio": "10:00",
  "hora_fim": "12:00"
}
🔗 Dependência Externa
Certifique-se de que a API de Gerenciamento Escolar esteja rodando em:

http://localhost:5000
Ela deve ter os seguintes endpoints funcionais:

GET /turmas/<id>

(opcional) GET /alunos/<id>

📁 Estrutura do Projeto
Reserva_de_salas_flask/
│
├── app.py
├── config.py
├── database.py
├── reserva_model.py
├── reserva_route.py
├── instance/
│   └── reservas.db
└── README.md
🛠️ Futuras Melhorias
Validação de conflito de horário

Integração via RabbitMQ ou outra fila

Autenticação e autorização de usuários

Logs e monitoramento com ferramentas externas
