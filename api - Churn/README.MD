# Minha API

Este projeto faz parte da entrega do MVP da Pós de Engenharia de Software, da Sprint de Qualidade de Software, Segurança e Sistemas Inteligentes.

O objetivo do projeto era a criação de uma SPA que usasse um modelo de classificação escolhido para analisar dados. O modelo escolhido foi o de classificação de rotatividade de clientes, prevendo se após o fim da assinatura ele continuaria ou não usando o serviço.

A maior parte do projeto pode ser aproveitada da primeira Sprint, como a criação do banco de dados em SQLite e também das APIs /listcliente, /addcliente e /delcliente.

A rota /listcliente serve para mostrar todos os clientes que existem no basnco de dados, a rota /asscliente serve para adicionar as informações do cliente no banco de daod através do front criado. E por último a /delcliente serve para deletar o cliente do banco de dados, tendo que ser colocada todas as colunas visto que somente todas elas juntas formam um cliente único.



## Como executar 
Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

USAR scikit-learn 1.2.2 para evitar erro!!!