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
  
  <br>

---

### Aula 24/03/2025

#### Amazon S3 Lifecycle

- Regras de Ciclo de Vida: Permitem gerenciar automaticamente os objetos armazenados no S3 ao longo do tempo.
- Transições de Classe de Armazenamento: Mover objetos entre classes de armazenamento com base em padrões de acesso.
  - Exemplo: Após 30 dias, mover de S3 Standard para S3 Standard-IA.
- Expiração de Objetos: Configurar para excluir automaticamente objetos que não são mais necessários.
  - Exemplo: Excluir backups antigos após 90 dias.
- Benefícios:
  - Redução de custos ao mover dados para classes de armazenamento mais baratas.
  - Gerenciamento automatizado, reduzindo a necessidade de intervenção manual.

#### Amazon S3 Versioning

- Permite manter múltiplas versões de um objeto no mesmo bucket.
- Ajuda a proteger contra exclusões acidentais e substituições de dados.
- Cada versão de um objeto recebe um identificador único.
- Pode ser habilitado ou desabilitado em nível de bucket.
- Benefícios:
  - Recuperação de versões anteriores de objetos.
  - Proteção contra exclusão acidental, pois objetos excluídos podem ser restaurados.
- Considerações:
  - Uma vez usado, da pra somente pausar ele.
  - Aumenta o custo de armazenamento, pois todas as versões são mantidas.
  - É recomendado combinar com regras de ciclo de vida para gerenciar versões antigas.

#### CORS

- É utilizado para controlar quais origens têm permissão para acessar recursos em um servidor.
- No Amazon S3, o CORS é configurado para permitir que aplicações hospedadas em diferentes domínios acessem os objetos armazenados no bucket.
- Cada regra pode especificar:
  - Métodos HTTP permitidos, como GET, POST, PUT.
  - Cabeçalhos que podem ser enviados pela origem.
  - Cabeçalhos que podem ser expostos para a aplicação cliente.
- Exemplo de uso: Permitir que um site hospedado em um domínio específico acesse imagens armazenadas em um bucket S3.

### Aula 24/03/2025

## Aula 05/05/2025
## Amazon VPC
### Introdução ao Amazon VPC

O Amazon Virtual Private Cloud (VPC) permite que você provisione uma seção isolada da nuvem AWS onde pode lançar recursos da AWS em uma rede virtual que você define. Ele oferece controle total sobre o ambiente de rede, incluindo seleção de intervalos de IP, criação de sub-redes e configuração de tabelas de roteamento e gateways de rede.

#### Componentes Principais do VPC

1. **Sub-redes:**
  - Dividem o VPC em segmentos menores.
  - Podem ser públicas (acessíveis pela internet) ou privadas (restritas a uma rede interna).

2. **Internet Gateway (IGW):**
  - Permite que instâncias em sub-redes públicas se comuniquem com a internet.

3. **NAT Gateway:**
  - Permite que instâncias em sub-redes privadas acessem a internet sem serem diretamente acessíveis.

4. **Tabelas de Roteamento:**
  - Definem como o tráfego é roteado dentro do VPC e para fora dele.

5. **Security Groups e Network ACLs:**
  - Controlam o tráfego de entrada e saída para instâncias e sub-redes.

#### Benefícios do Amazon VPC

- **Isolamento:** Recursos são isolados em uma rede virtual privada.
- **Segurança:** Controle granular sobre o tráfego de rede.
- **Flexibilidade:** Personalização de configurações de rede para atender às necessidades específicas.
- **Conectividade Híbrida:** Integração com redes locais usando VPN ou AWS Direct Connect.

#### Casos de Uso

- Hospedagem de aplicativos web em sub-redes públicas com bancos de dados em sub-redes privadas.
- Configuração de ambientes híbridos conectando redes locais ao VPC.
- Implementação de arquiteturas de microserviços com controle de tráfego entre serviços.

#### Boas Práticas

- Use múltiplas zonas de disponibilidade (AZs) para alta disponibilidade.
- Configure sub-redes privadas para recursos sensíveis.
- Habilite logs do VPC Flow para monitorar o tráfego de rede.
- Utilize Security Groups e Network ACLs para reforçar a segurança.

#### Aula 05/05/2025

### CIDR (Classless Inter-Domain Routing)

- Define o intervalo de endereços IP disponíveis em um VPC.
- Representado no formato `x.x.x.x/n`, onde `n` indica o número de bits da máscara de rede.
  - Exemplo: `10.0.0.0/16` define um intervalo de 65.536 endereços IP.
- Permite dividir o espaço de endereços em sub-redes menores.

### Subnet Pública

- Sub-rede configurada para permitir acesso direto à internet.
- Requisitos:
  - Associada a uma tabela de roteamento com um **Internet Gateway (IGW)**.
  - Instâncias na sub-rede devem ter um **Elastic IP** ou **Public IP**.
- Usada para hospedar recursos que precisam ser acessíveis publicamente, como servidores web.
- Benefícios:
  - Facilita a comunicação com a internet.
  - Ideal para serviços que requerem alta disponibilidade pública.
- Considerações:
  - Reforçar a segurança com **Security Groups** e **Network ACLs**.


#### Aula 12/05/2025

### Laboratórios Canvas

#### Guided Lab: Creating a Virtual Private Cloud
#### Challenge Lab: Creating a VPC Networking Environment for the Café


### Aula 15/05/2025

#### Laboratórios Canvas

- **Guided Lab:** Creating a Virtual Private Cloud
  - Objetivo: Aprender a criar e configurar um VPC com sub-redes públicas e privadas, tabelas de roteamento e gateways.
  - Passos:
    1. Criar um VPC com um intervalo CIDR apropriado.
    2. Configurar sub-redes públicas e privadas.
    3. Associar tabelas de roteamento às sub-redes.
    4. Configurar um Internet Gateway para a sub-rede pública.
    5. Criar um NAT Gateway para permitir que a sub-rede privada acesse a internet.

- **Challenge Lab:** Creating a VPC Networking Environment for the Café
  - Objetivo: Implementar um ambiente de rede para um cenário de café, utilizando as melhores práticas de VPC.
  - Passos:
    1. Criar um VPC com múltiplas zonas de disponibilidade.
    2. Configurar sub-redes públicas para servidores web e sub-redes privadas para bancos de dados.
    3. Implementar regras de segurança com Security Groups e Network ACLs.
    4. Configurar logs do VPC Flow para monitorar o tráfego de rede.
    5. Testar a conectividade entre os recursos e validar a configuração.

- **Resultados Esperados:**
  - Compreensão prática de como criar e gerenciar um VPC.
  - Habilidade de configurar ambientes de rede seguros e escaláveis na AWS.


#### Aula 19/05/2025

### VPC Peering

- Permite conectar dois VPCs para que possam se comunicar diretamente, como se estivessem na mesma rede.
- **Características:**
  - Comunicação ponto a ponto entre VPCs.
  - Pode ser configurado entre VPCs na mesma conta ou em contas diferentes.
  - Não suporta transitividade (se A está conectado a B, e B a C, A não pode se comunicar com C).
- **Casos de Uso:**
  - Compartilhamento de recursos entre VPCs.
  - Comunicação entre ambientes de produção e desenvolvimento.
- **Boas Práticas:**
  - Planejar intervalos CIDR para evitar sobreposição de endereços IP.
  - Configurar regras de segurança nos Security Groups e Network ACLs.

### AWS VPN Site-to-Site

- Permite conectar uma rede local a um VPC usando uma conexão VPN segura.
- **Características:**
  - Usa o protocolo IPsec para criptografar o tráfego.
  - Requer um Customer Gateway (CGW) na rede local e um Virtual Private Gateway (VGW) no VPC.
- **Casos de Uso:**
  - Extensão de redes locais para a nuvem.
  - Comunicação segura entre data centers e AWS.
- **Benefícios:**
  - Custo mais baixo em comparação com conexões dedicadas.
  - Configuração rápida e flexível.
- **Considerações:**
  - Latência pode variar dependendo da qualidade da conexão de internet.
  - Recomendado para cargas de trabalho que não exigem alta largura de banda.

---

### AWS Direct Connect

- Fornece uma conexão de rede dedicada entre uma rede local e a AWS.
- **Características:**
  - Conexão física com alta largura de banda e baixa latência.
  - Pode ser combinada com VPN para maior segurança.
- **Casos de Uso:**
  - Transferência de grandes volumes de dados.
  - Aplicações que exigem baixa latência e alta consistência.
- **Benefícios:**
  - Reduz custos de transferência de dados em comparação com conexões baseadas na internet.
  - Maior confiabilidade e desempenho.
- **Considerações:**
  - Requer tempo e custo para instalação.
    - Ideal para empresas com necessidades de conectividade de longo prazo.

  #### Aula 26/05/2025

  ### IAM Groups

  - Permitem agrupar usuários com permissões semelhantes.
  - Facilita a gestão de permissões em larga escala.
  - Exemplo: Grupo "Desenvolvedores" com acesso a recursos de desenvolvimento.

  ### Roles - AWS STS (Security Token Service)

  - Roles permitem delegar permissões temporárias a usuários, aplicações ou serviços.
  - AWS STS gera credenciais temporárias para acessar recursos.
  - Casos de uso:
    - Permitir que aplicações acessem recursos sem armazenar credenciais fixas.
    - Usuários externos (como parceiros) acessando recursos de forma controlada.
  - Benefícios:
    - Reduz riscos de exposição de credenciais.
    - Permissões podem ser limitadas em escopo e tempo.

  ### AWS Cognito

  - Serviço gerenciado para autenticação, autorização e gerenciamento de usuários.
  - Permite adicionar login social (Google, Facebook, etc.) e login corporativo (SAML, OIDC).
  - Gerencia identidades de usuários e fornece tokens de acesso para aplicações.
  - Integração fácil com aplicações web e mobile.
  - Recursos:
    - Pools de usuários (User Pools) para autenticação.
    - Pools de identidades (Identity Pools) para acesso federado a recursos AWS.
  - Segurança:
    - Suporte a MFA, políticas de senha e monitoramento de atividades.

### Aula 29/05/2025

#### Criptografia Simétrica

- Utiliza a mesma chave para criptografar e descriptografar dados.
- É rápida e eficiente para grandes volumes de dados.
- Exemplo de algoritmos: AES, DES.
- Desafio principal: distribuição segura da chave entre as partes.

#### Criptografia Assimétrica

- Utiliza um par de chaves: uma pública e uma privada.
- A chave pública criptografa os dados e apenas a chave privada correspondente pode descriptografar.
- Exemplo de algoritmos: RSA, ECC.
- Usada para troca segura de chaves, autenticação e assinatura digital.
- Mais lenta que a simétrica, geralmente usada em conjunto com ela para garantir segurança e desempenho.


### Aula 16/06/2025

#### Load Balancer

- Distribui automaticamente o tráfego de entrada entre múltiplos destinos, como instâncias EC2, containers ou endereços IP.
- **Tipos de Load Balancers na AWS:**
  - **Application Load Balancer (ALB):** Camada 7 (HTTP/HTTPS), ideal para aplicações web.
  - **Network Load Balancer (NLB):** Camada 4 (TCP/UDP), alta performance e baixa latência.
  - **Gateway Load Balancer (GWLB):** Para appliances virtuais de segurança.
  - **Classic Load Balancer (CLB):** Legado, suporta tanto camada 4 quanto 7.

- **Benefícios:**
  - Alta disponibilidade através de distribuição de carga.
  - Detecção automática de instâncias não saudáveis (health checks).
  - Escalabilidade automática baseada na demanda.
  - Integração com Auto Scaling Groups.

- **Configurações Importantes:**
  - Health checks para monitorar status das instâncias.
  - Target Groups para agrupar destinos.
  - Listeners para definir portas e protocolos.
  - SSL/TLS termination para criptografia.

#### DNS (Domain Name System)

- Sistema que traduz nomes de domínio legíveis por humanos em endereços IP.
- **Amazon Route 53:**
  - Serviço DNS gerenciado da AWS.
  - Alta disponibilidade e escalabilidade global.
  - Suporte a diferentes tipos de registros (A, AAAA, CNAME, MX, etc.).

- **Políticas de Roteamento:**
  - **Simple:** Roteamento básico para um único recurso.
  - **Weighted:** Distribui tráfego com base em pesos atribuídos.
  - **Latency-based:** Roteia para o recurso com menor latência.
  - **Failover:** Roteamento ativo-passivo para alta disponibilidade.
  - **Geolocation:** Roteamento baseado na localização do usuário.
  - **Geoproximity:** Roteamento baseado na proximidade geográfica.

### Aula 23/06/2025

#### Infraestrutura como Código (IaC)

- Prática de gerenciar e provisionar infraestrutura através de código ao invés de processos manuais.
- **Vantagens:**
  - **Consistência:** Ambientes idênticos podem ser criados repetidamente.
  - **Versionamento:** Mudanças na infraestrutura podem ser rastreadas e versionadas.
  - **Automação:** Reduz erros humanos e acelera deployments.
  - **Documentação:** O código serve como documentação da infraestrutura.

- **Ferramentas AWS para IaC:**
  - **AWS CloudFormation:**
    - Serviço nativo para definir infraestrutura usando templates JSON/YAML.
    - Gerencia dependências entre recursos automaticamente.
    - Rollback automático em caso de falhas.
    - Stacks para organizar recursos relacionados.

  - **AWS CDK (Cloud Development Kit):**
    - Define infraestrutura usando linguagens de programação familiares.
    - Suporte para TypeScript, Python, Java, C#, Go.
    - Compila para templates CloudFormation.
    - Maior flexibilidade para lógica complexa.

- **Boas Práticas:**
  - Usar controle de versão (Git) para templates.
  - Implementar testes automatizados para templates.
  - Separar configurações por ambiente (dev, staging, prod).
  - Utilizar parâmetros e outputs para flexibilidade.
  - Implementar políticas de segurança no código.

- **Conceitos Importantes:**
  - **Immutable Infrastructure:** Substituir ao invés de modificar recursos.
  - **GitOps:** Usar Git como fonte da verdade para estado da infraestrutura.
  - **Drift Detection:** Identificar diferenças entre estado desejado e atual.

#### AUla 26/06/2025

  ### Como Reduzir Acoplamento das Aplicações

  - **Separar responsabilidades:** Divida o sistema em modulos ou serviços com funçoes bem definidas
  - **Interfaces bem definidas:** Use API ou contratos claros para comunicação entre componentes.
  - **Injecao de dependencia:** Permite trocar implementações sem alterar o código principal.
  - **Mensageria/Filas:** Use filas para desacoplar produtores e consumidores de dados.
  - **Evite dependencias diretas:** Prefira abstrações doq chamadas diretas entre modulos.
  - **Documentacao:** Mantenha contratos e integrações bem documentados para facilitar mudanças.