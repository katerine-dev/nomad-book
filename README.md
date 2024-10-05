# nomad-book

Full stack application to manage travel itinerary

## Venv 

Ativando o Ambiente Virtual:
```sh
poetry shell
```

Adicionando novas dependências:
```sh
# The line below adds the `requests` library
poetry add requests
```

Instalando o projeto com todas as depedências já declaradas:
```sh
poetry install
```

Para criar uma imagem no docker:
```sh
docker run -d \
    --rm \
    --name nomadbook \
    -e POSTGRES_PASSWORD=nomadbook \
    -e POSTGRES_USER=nomadbook \
    -e POSTGRES_DB=nomadbook \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```

Migrations List:
```sh
yoyo list 
```
For Apply Migrations:
```sh
yoyo apply
```

For run the server:
```sh
uvicorn nomadbook.main:app --host 0.0.0.0 --port 8000
```
