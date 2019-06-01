# moc_banco

## Limpar ambiente

```sh
docker stop $(docker ps -q -a)
docker rm -f $(docker ps -q -a)
docker volume prune -f
docker rmi -f $(docker images -q -a)
```

## Configuração do container do postgres
```sh
docker build -t moc .
docker run --name="mocbanco_db" -p 5432:5432 -v local_mocbanco:/var/lib/postgresql/data moc
```

## Executar as migrações
```sh
python migrations.py db init
python migrations.py db migrate
python migrations.py db upgrade
```

## Executar a aplicação local
```sh
python migrations.py runserver
```
