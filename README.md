# UnbFeelings_api

## inicializando projeto para desenvolvimento

* De um ```git clone <url-do-repositorio>```

* Instale o docker e o docker-compose em seu computador para usar com o sudo (administrador) - padrão

* Execute o comando
```
docker-compose up --build -d
```

* Em seguida execute o comando
```
docker exec -it <nome_do_container> bash
```
* Com isso você estará dentro do terminal do container e poderá criar um super usuário via shell (por algum motivo o ```python manage.py createsuperuser``` não está funcionando)

* Com isso você pode modificar os arquivos localmente em sua máquina que ele serão automaticamente modificados dentro do container, possibilitando assim ter um ambiente de desenvolvimento sem a necessidade de muita configuração do ambiente.