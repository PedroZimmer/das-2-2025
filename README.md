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

## Securing Access
#### Aula 10/03/2025

### Modelo de Responsabilidade Compartilhada

- Em sistemas **on-premise**, a responsabilidade é do usuário.
- Na **nuvem**, a responsabilidade é compartilhada:
  - AWS cuida da infraestrutura física (servidores, racks, energia, etc.).
  - O usuário é responsável pela configuração e segurança de seus recursos.

##### Exemplo:
- Se um servidor foi invadido porque a porta 22 estava aberta e a senha era fraca, a culpa é do usuário.
- Se a falha for de um software da AWS, a responsabilidade é da AWS.

### Segurança no S3

O S3 é um meio-termo entre SaaS e PaaS. Nele, a AWS é responsável por:
- Rede
- Firewall
- Sistema Operacional

##### Server-Side Encryption (SSE)

Modelos de criptografia no S3:
- **SSE-S3:** AWS gera e gerencia a chave.
- **SSE-KMS:** O usuário gerencia a chave pelo Key Management Service (KMS).
- **SSE-C:** O usuário fornece a chave de criptografia.

Caso de ataque:
- Hackers alteraram a configuração de um bucket para usar **SSE-C**, permitindo que apenas eles tivessem a chave de descriptografia.

### Princípios para Aplicações Seguras

- **Identidade e Acesso:** Use provedores como Keycloak para evitar armazenar senhas diretamente.
- **Proteção de Dados:**
  - Em trânsito: **SSL/TLS (HTTPS)**
  - Em repouso: **Criptografia em disco (EBS, S3)**
  - Em uso: **Criptografia da RAM (Intel Enclave, AMD SEV)**
- **Camadas de Segurança:**
  - Firewall e antivírus não são suficientes.
  - Controle de acesso e monitoramento são essenciais.
- **Rastreabilidade:**
  - Registrar atividades dos usuários para auditoria.
- **Automatização de Segurança:**
  - Criar usuários manualmente leva a erros.
  - Implementar boas práticas de segurança automatizadas.

### Autenticação e Autorização

- **Autenticação:** Verifica identidade.
  - Exemplo: Login e senha, biometria, token físico.
- **Autorização:** Define permissões.
  - Exemplo: IAM Policy para limitar acessos na AWS.
- **Princípio do Privilégio Mínimo:**
  - Usuários só devem ter acesso ao que realmente precisam.

---

#### Aula 13/03/2025

### Revisão da Aula Anterior
- Modelo de responsabilidade compartilhada
- Princípio do privilégio mínimo
- Autenticação e autorização
- Identity and Access Management (IAM)

### Meios de Acesso à AWS
- **Console Web**
- **Acesso Programático (AWS CLI)**

### Configuração de Acesso Programático
- **IAM User** e **IAM Group**
- **Access Key** e **Secret Key**
- **Melhores práticas:**
  - Habilitar **MFA**
  - Definir **expiração da conta**

### Usuário Root
- Conta **master** da AWS, pode fazer tudo.
- Deve ter **MFA habilitado**.
- **Nunca usar no dia a dia**.

### IAM Roles
- Permitem assumir diferentes permissões temporariamente.
- **Exemplo:** Funcionário muda de função temporariamente (como um cozinheiro assumindo o caixa).
- **Vantagem:** Sessões expiram automaticamente, minimizando riscos.

### Instance Profile
- Associa credenciais diretamente a uma máquina virtual (EC2).
- Evita armazenar **chaves de acesso** diretamente na aplicação.


---

#### Aula 17/03/2025

### RBAC - Role Basic Access Control

Polices gerenciáveis e não gerenciáveis

- **Polices Gerenciáveis:**
  - Criadas e mantidas pela AWS.
  - Podem ser aplicadas a múltiplos usuários, grupos ou roles.

- **Polices Não Gerenciáveis:**
  - Criadas pelo usuário.
  - Customizadas para atender necessidades específicas.
  - Exemplo: Uma polic que permite acesso de leitura a um bucket S3 específico.

### Princípios do RBAC

- Dividir responsabilidades para minimizar riscos. 
- Conceder apenas as permissões necessárias para realizar uma tarefa.
- Reduz a superfície de ataque e o impacto de possíveis compromissos.
- Registrar e monitorar atividades para detectar e responder a incidentes de segurança.

### Implementação do RBAC na AWS

1. **Definir Funções:**
  - Identificar funções na organização (ex.: administrador, desenvolvedor).

2. **Criar Grupos e Roles:**
  - Criar grupos no IAM e associar roles específicas.

3. **Atribuir Polices:**
  - Aplicar polices gerenciáveis ou não gerenciáveis, seguindo o princípio do privilégio mínimo.

4. **Revisar Regularmente:**
  - Revisar e atualizar permissões periodicamente conforme necessário.

---
### IAM Policy estrutura de documento

Uma política IAM é um documento JSON que define permissões. Estrutura básica:

- **Version:** Data do formato da política.
- **Statement:** Lista de permissões.
  - **Effect:** Permitir ou negar acesso.
  - **Action:** Ações permitidas ou negadas.
  - **Resource:** Recursos aos quais a política se aplica.
  - **Conditioon:** Define condições específicas para a aplicação da política.
    - Exemplo: Permitir acesso apenas de um endereço IP específico.


### Tipos de aramzenamneot me nuvem

- Por blocos / "blocados" -> EBS elastic block storage
  - SSD, HDD
- File share -> FXs/EFS elastic fire system
  - Um servidor onde todos se conectam nele, ele resolve conflitos tambem, ao varios usuarios tentarem modificar o mesmo arquivo.
- De objeto -> s3
  - Baseado em atributos e metadados


#### Aula 20/03/2025

## Beneficios S3

- Alta Performance
- Durabilidade
- Availability


#### How customers use AWS S3
- Spikes in demand
- Static Site
- Financial Analysis
- Disaster recovery

#### Object Storage Classes

- forma como o s3 guarda a informacao
  - define o preco 
  - disponibildade do arquivo
- Classes quentes
  - Acesso imediato
- Classes frias
  - Precisam ser 'rehidratados'

- general purpose
  - S3 Standard
    - Maior diponibildade
    - Preco de download barato
    - Mais caro para armazenar

- Intelligent tiering
  - S3 Intelligent-Tiering
    - Ele monitora o comportamento do arquivo
    - E guarda ele nos Glacier de acordo com a demanda dele


- Infrequent Access
  - S3 Standard-IA
    - Mais caros para baixar
    - mais barato para armazenar
    - 3 copias
    - 
  - S3 One Zone-IA
    - Mais barato para guardar
    - Acesso infrequente
    - Poucos acessos
    - Faz somente uma copia do objeto
    - Perde durabilidade
- Archive (GElados)
  - S3 Glacier Instant Retrieval
    - Volta quase instantaneamente
    - O mais caro dos Glacier
    - 
  - S3 Glacier Deep Archive
    - O mais barato para guardar
    - O mais caro para tirar
    - Demora muito para retornar o arquivo 
    - POde levar dias para reotrnar
  - S3 Glacier Flexible Retrieval
    - Ele volta o arquivo mais rapido
    - Consequentemete mais caro
    - Minutos para voltar
  - S3 on Outposts