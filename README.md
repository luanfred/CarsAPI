### README para a API de Carros com FastAPI

# API de Carros com FastAPI

Este projeto é uma **API RESTful** simples e eficiente para gerenciar uma coleção de carros, construída com **FastAPI**. A aplicação usa **PostgreSQL** como banco de dados e é totalmente containerizada com **Docker Compose**, simplificando a configuração e a execução.

-----

### Instalação e Execução

Para colocar a API em funcionamento rapidamente, siga os passos abaixo.

#### 1\. Clonar o Repositório

Comece clonando o projeto do GitHub e navegando para a pasta principal.

```bash
git clone https://github.com/luanfred/CarsAPI.git
cd CarsAPI
```

#### 2\. Configurar o Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais do banco de dados.

Abra o arquivo `.env` e adicione as seguintes variáveis, substituindo os valores `seu_usuario` e `sua_senha` pelas suas informações.

```bash
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=cars_db
DATABASE_URL=postgresql://seu_usuario:sua_senha@db:5432/cars_db
```

#### 3\. Iniciar com Docker

Com o Docker Compose, a construção da imagem e a inicialização dos serviços (API e banco de dados) são feitas com um único comando.

```bash
docker compose up --build
```

Aguarde alguns instantes até que os serviços sejam iniciados.

-----

### Endpoints da API

A API oferece uma variedade de endpoints para realizar operações **CRUD** (Criar, Ler, Atualizar, Deletar) em carros.

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/cars` | Lista todos os carros cadastrados. |
| `POST` | `/cars` | Adiciona um novo carro. |
| `PUT` | `/cars/{car_id}` | Atualiza um carro existente, usando seu ID como referência. |
| `DELETE` | `/cars/{car_id}` | Remove um carro pelo seu ID. |

-----

### Documentação Interativa

Após iniciar a aplicação, a documentação interativa da API estará disponível nos seguintes endereços:

  * **Swagger UI**: `http://localhost:8000/docs`
  * **ReDoc**: `http://localhost:8000/redoc`

Você pode usar essas interfaces para testar os endpoints diretamente no navegador.
