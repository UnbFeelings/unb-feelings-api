# UnbFeelings_api

[![Coverage Status](https://coveralls.io/repos/github/UnbFeelings/unb-feelings-api/badge.svg?branch=devops)](https://coveralls.io/github/UnbFeelings/unb-feelings-api?branch=devops)
[![pipeline status](https://gitlab.com/UnbFeelings/unb-feelings-api/badges/master/pipeline.svg)](https://gitlab.com/UnbFeelings/unb-feelings-api/commits/master)

***

Para subir os ambientes do UnB Feelings API, primeiramente é necessário instalar o docker e o docker-compose em seu computador.

## Ambiente de Desenvolvimento

* Para clonar o repositório execute o comando:
```bash
git clone https://github.com/UnbFeelings/unb-feelings-api.git
```

* Para subir o ambiente basta fazer:
```bash
sudo docker-compose build
sudo docker-compose run dev python manage.py migrate
```
* Esse primeiro passo só é necessário uma vez. Mas você precisará executar uma nova build sempre que um novo pacote pip for adicionado aos requirements.

E para executar:
```bash
sudo docker-compose up
```
* Após executar o ultimo comando, o servidor estará rodando na url 0.0.0.0:8000.

Lembrando que sempre que uma model for alterada, será necessário atualizar/criar a sua devida migração.
```bash
sudo docker-compose run dev python manage.py makemigrations
```
E realizar essa migração no banco:
```bash
sudo docker-compose run dev python manage.py migrate
```

* Para entrar no terminal do container utilize o seguinte comando
```
docker exec -it <nome_do_container> bash
```

* Com isso você estará dentro do terminal do container e poderá criar um super usuário via shell.
O ```python manage.py createsuperuser``` não está funcionando
devido ao usuário precisar de um curso, então para criar um usuário é necessário entrar via shell pegar(ou criar) um curso e usa-lo na criação do usuário.

* Com isso você pode modificar os arquivos localmente em sua máquina que ele serão automaticamente modificados dentro do container, possibilitando assim ter um ambiente de desenvolvimento sem a necessidade de muita configuração do ambiente.

## Ambiente de Testes

* Para rodar os testes, execute o seguinte comando para subir o ambiente de teste
```
sudo docker-compose run dev python manage.py test
```

Também é possível executar os testes pelo mesmo docker do CI:
```bash
sudo docker-compose -f compose/test/docker-compose.test.yml build
sudo docker-compose -f compose/test/docker-compose.test.yml run unbfeelings-test python manage.py test
```

Mas nesse caso, é mais fácil simplismente fazer um _push_ para a sua branch no github que logo o CI irá automaticamente executar os testes.

Agora caso queira ver a cobertura de testes:
```bash
sudo docker-compose run dev coverage run --source='.' manage.py test
sudo docker-compose run dev coverage report
```

Caso queira uma analise mais detalhada da cobertura, basta olhar o submit da cobertura pelo CI para o _coveralls_, ou, em vez de ```coverage report``` executar ```coverage html``` e uma pasta de nome __htmlcov__ será criada com a cobertura em HTML.
