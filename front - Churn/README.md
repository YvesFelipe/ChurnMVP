# Meu Front

Este projeto faz parte da entrega do MVP da Pós de Engenharia de Software, da Sprint de Qualidade de Software, Segurança e Sistemas Inteligentes

O objetivo do projeto era a criação de uma SPA que usasse um modelo de classificação escolhido para analisar dados. O modelo escolhido foi o de classificação de rotatividade de clientes, prevendo se após o fim da assinatura ele continuaria ou não usando o serviço.

Para a realização da entrada dos dados foram criados campos e dropwdowns para inserir as informações. As colunas Age,Tenure, Usage Frequency, Support Calls, Payment Delay,Total Spend, Last Interaction usavam de campos que aceitavam somente números e as colunas Gender,Subscription Type,Contract Length usavam de dropdowns com as opções oferecidas.

Após a entrada dos dados, o modelo era chamado para fazer a classificação do cliente e na parte de baixo, a tabela mostra através da API /listcliente todos os clientes no banco de dados como também a classificação de rotatividade que ele recebeu, tendo também a direita da coluna Churn a opção de deletar o cliente ao clicar no "X".

---
## Como executar

Basta fazer o download do projeto e abrir o arquivo index.html no seu browser.
