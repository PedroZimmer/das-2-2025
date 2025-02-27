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