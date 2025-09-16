# API de Carros FastAPI

Este projeto é uma aplicação FastAPI que fornece uma API RESTful para gerenciamento de carros. Utiliza PostgreSQL como banco de dados e suporta operações CRUD completas.


## Instruções de Instalação

1. **Clone o repositório:**
   ```
   git clone https://github.com/luanfred/CarsAPI.git
   cd CarsAPI
   ```

2. **Construa e execute a aplicação com Docker Compose:**
   ```
   docker compose up --build
   ```

3. **Acesse a API:**
   A API estará disponível em http://localhost:8000. Você pode acessar a documentação interativa da API através do Swagger em http://localhost:8000/docs ou do ReDoc em http://localhost:8000/redoc. 

   Você também pode utilizar ferramentas como Postman ou curl para interagir com os endpoints.

## Uso

### Endpoints

- **GET /cars**: Lista todos os carros.
- **POST /cars**: Adiciona um novo carro.
- **PUT /cars/{car_id}**: Atualiza um carro existente pelo ID.
- **DELETE /cars/{car_id}**: Remove um carro pelo ID.
