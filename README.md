## Design e Arquitetura de Software II
#### PEDRO ECCEL ZIMMERMANN


- ##### 27/02/2025:

####  Design Trade-off 

As you design a solution, think carefully about trade offs so you can select an optimal approach.

- Evaluate trade off so you can select an optimal approach

###### Examples:
    - Trade consistency, durability, and space for time and latency to deliver higer performance

    - For new features, prioritize speed to market over cost

    - Base design decisions on empirical data

Abre mao da durabilidade para ter performance (cache)

##### Elasticidade do servidor:

A linguagem de programação te um limite de operações, se chegar a esse limite o servidor cai, nesse caso teria que ter mais servidores disponiveis automaticamente

  +Consistencia
  +Disponibilidade
  +Gasto Mais Dinheiro


##### Automating your enviroment:

se a minha maquina crashar, tem que ter um detector que deu ruim/caiu a maquina, com isso a AWS reconstroi a maquina similar para conseguir suprir a demanda enquanto esta sendo feita a manutencao


- #### 06/03

##### Infraestrutura como codigo IAC

Tratar seus recursos como descartaveis

Automate deployment of new resources with identical configurations
Stop resources that are not in use
Test updates on new resources, and thne replace...

##### Acomplamento

Desenha a arquitetura com componentes independentes
Consiga trocar componentes facilmente (Exemplo: HDMI, um dispositovo que conte hdi consegue rodar em varios outros que tambem possuam hdmi)
Cria replicas do DB, coloca um ELB para mostrar qual DB vai ser usado para melhorar a performance
O ELB tambem checa se a maquina do DB esta viva, antes de mandar a informcao, verifica se ela esta ativa.
- ###### Para ter alta diponibilidade voce precisa ter redundancia.


##### Desenhe servicos nao servidores

- Quando possivel considere usar containers ou serverless
- Message queues
- Static WEB assests can be stores off server, such as on Amaon Sim Storage Service (Amazon S3)
- User Authentication with AWS

##### Escolha a melhor solucao de banco de dados

Relacional ou Nao relacional

O relacional tem um problema: Escalabilidade horinzontal:
Tem um limite de replicas do banco original, diferente do Nosql, que foi feito para ser escalado horinzontalmente e nao verticalmente. Entao o relacional tem limite ja o nosql nao.

NoSQL: muita performance

##### Otimizacao de custo

Na AWS, nao querem que voce gaste muito.

#### Usando Caching

Melhora a performance e custo

