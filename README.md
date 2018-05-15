# UnbFeelings_api

Para subir os ambientes do UnB Feelings API, primeiramente é necessário instalar o docker e o docker-compose em seu computador.

## Ambiente de Desenvolvimento

* Para clonar o repositório execute o comando: 
```
git clone git@github.com:ejplatform/ej-server.git
```

* Para subir o ambiente de produção execute o seguinte comando:
```
sudo docker-compose -f up --build
```

* Após executar o ultimo comando, o servidor estará rodando na url 0.0.0.0:8000.

* Para entrar no terminal do container utilize o seguinte comando
```
docker exec -it <nome_do_container> bash
```

* Com isso você estará dentro do terminal do container e poderá criar um super usuário via shell (por algum motivo o ```python manage.py createsuperuser``` não está funcionando)

* Com isso você pode modificar os arquivos localmente em sua máquina que ele serão automaticamente modificados dentro do container, possibilitando assim ter um ambiente de desenvolvimento sem a necessidade de muita configuração do ambiente.

## Ambiente de Testes

* Para rodar os testes, execute o seguinte comando para subir o ambiente de teste
```
sudo docker-compose -f compose/test/docker-compose.test.yml up
```

