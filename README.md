# Projeto de Engenharia de Software

## Metáfora do sistema

Imaginemos o sistema como uma biblioteca universitária que tenha salas de estudo, individuais e em grupo.

  1. Autenticação de usuário:
    Cada usuário possui seu identificador na biblioteca, um crachá, o qual permite que ele entre na biblioteca; esse seria o 'username' de cada usuário no sistema.
  2. Pesquisar livro:
    Seria como perguntar para a bibliotecária onde fica tal livro e ela te mostraria as opções de acordo com sua descrição.
  3. Gerar meta de leitura:
    Seria análogo a reservar uma sala de estudos por um determinado tempo para ler um livro ou partes de um livro em específico, nesse momento a pessoa que reservou a sala se tornaria responsável (adiministradora ou editora) pela sala.
      - Gerar meta de leitura pública: reservar a sala e avisar à recepção que qualquer um pode participar dessa sala.
  4. Entrar em uma meta de leitura:
    Ao ser Convidado por um responsável pela sala, o usuário pode se registrar para frequentar uma sala e se propor a cumprir a meta daquela sala.
      - Entrar em uma meta pública: pedir para a recepção as salas com atividades públicas e fazer o registro para participar da atividade da sala.
  5. Atualizar o progresso de leitura:
    O usuário assim que pausa sua leitura escreve num canto do quadro branco da sala a página onde parou.


## Casos de uso

### Autenticação, conta e perfil

1. Atualização do Perfil do Usuário
  - **Atores:** usuário registrado e sistema.
  - **Descrição:** o usuário deseja poder atualizar as informações do seu perfil.
  - **Fluxo Principal:**
    1. O usuário faz login na sua conta.
    2. O usuário navega até a seção de "Perfil" do aplicativo.
    3. O usuário pode editar informações como nome, foto de perfil e outras informações relevantes.
    4. O usuário salva as alterações no seu perfil.
2. Recuperação de Senha
  - **Atores:** usuário registrado e sistema.
  - **Descrição:** o usuário esqueceu sua senha e deseja redefini-la de forma segura.
  - **Fluxo Principal:**
    1. O usuário acessa a tela de login do aplicativo.
    2. O usuário clica na opção "Esqueci minha senha".
    3. O sistema solicita o endereço de e-mail do usuário.
    4. O sistema envia um e-mail de redefinição de senha para o endereço de e-mail fornecido.
    5. O usuário verifica seu e-mail e clica no link de redefinição de senha.
    6. O sistema permite que o usuário defina uma nova senha.
    7. O sistema confirma a alteração da senha e redireciona o usuário para a tela de login, onde ele pode acessar sua conta com a nova senha.

### Metas de leitura individuais

1. Atualizar meta de leitura existente.
  - **Atores:** usuário e sistema.
  - **Descrição:** o usuário deseja alterar dados de uma meta de leitura individual já criada.
  - **Fluxo principal:**
    1. O usuário faz login na sua conta.
    2. O usuário acessa a seção "Metas de leitura".
    3. O sistema apresenta o histórico de metas de leitura em andamento ou concluídas do usuário que não foram 
    4. O usuário encontra a meta de leitura que deseja modificar e a seleciona.
    5. O sistema exibe detalhes da meta de leitura selecionada, incluindo os prazos (datas) e os livros e páginas associadas a esses prazos.
    6. O usuário seleciona o botão "Editar".
    7. O sistema exibe uma tela semelhante a de criação de meta de leitura, mas com os dados já preenchidos conforme a meta sendo editada.
    8. O usuário seleciona e altera os dados que desejar, clicando em "Salvar" ao fim do processo.
    9. O sistema exibe uma mensagem indicando que os dados foram alterados com sucesso e retorna à página de metas de leitura.

2. Lembrar o usuário de metas de leitura.
  - **Atores:** sistema.
  - **Descrição:** O sistema exibe na tela inicial lembretes de metas de leitura não concluídas que não tiveram nenhum progresso registrado nos últimos dias.
  - **Fluxo principal:**
    1. Às 00h de cada dia, o sistema identifica dentre as metas de leitura não concluídas do usuário se a data da última atualização de progresso ultrapassa uma semana (7 dias).
    2. Caso alguma meta seja identificada, ela será exibida na tela inicial do usuário, junto com uma mensagem avisando o tempo que a meta está sem progresso registrado.
    3. Se existir mais de uma meta inativa, o sistema irá exibir todas elas na página inicial do usuário, em ordem de prioridade (isto é, no topo aparecerão as metas com prazo mais próximo).
    4. Caso alguma não receba atualização por mais de um mês e seu prazo termine, o sistema deverá exibí-la com prioridade, junto com um aviso informando sobre a possibilidade de editá-la ou excluí-la.

### Metas de leitura - estendido para múltiplas pessoas.

1. Entrar em uma meta existente:
  - **Atores:** Usuário e sistema
  - **Descrição:** O usuário deseja deseja entrar em uma meta de leitura já estabelecida por alguém.
  - **Fluxo Principal:**
    1. O usuário faz login à sua conta
    2. O usuário navega até a sessão de metas
    3. O entra em adicionar nova meta e vai em embarcar em meta existente e coloca o código que recebeu de algum amigo
    4. O sistema recebe o código, busca no banco de dados e cadastra ele naquela meta

2. Criar uma meta publica:
  - **Atores:** Usuário e sistema
  - **Descrição:** O usuário deseja criar uma meta publica
  - **Fluxo Principal:**
    1. O usuário faz login
    2. Navega até a sessão metas
    3. Entra em adicionar nova meta e vai em criar nova meta
    4. seleciona o livro desejado, com opção de livro completo, adiciona a data limite e informa que a meta é publica e a nomeia
    5. o sistema recebe as informações acima e cria a meta com o usuario como editor e coloca ela na lista de metas públicas para ser visualisada por todos que assim quiserem.

### Progresso de leitura

1. Atualizar o progresso:
- **Ator Principal:** Usuário e sistema
- **Descrição:** O usuário deseja atualizar o progresso de leitura de um livro no sistema de leituras.
- **Fluxo Principal:**
    1. O usuário faz login na sua conta
    2. O usuário navega até a lista de livros atualmente em leitura
    3. O usuário seleciona o livro que deseja atualizar
    4. O usuário insere o progresso da leitura (número de páginas lidas).
    5. O sistema registra a atualização do progresso no banco de dados do usuário e atualiza o status do livro.

2. Acompanhar progressos de leitura em metas de leitura compartilhadas
- **Atores:** Usuário e sistema
- **Descrição:** Acompanhar os progressos de leitura de outros usuários que participam de uma meta de leitura compartilhada com o usuário em um livro específico.
- **Fluxo Principal:**
    1. O usuário faz login na sua conta
    2. O usuário acessa a página da meta de leitura conjunta
    3. O sistema exibe a lista de membros que estão participando da meta de leitura conjunta no livro específico
    4. O usuário pode ver o progresso de leitura de cada membro do grupo para o livro em questão, incluindo o número de páginas lidas ou a porcentagem concluída
    5. O usuário pode acompanhar o progresso dos outros membros do grupo e interagir, como comentar ou encorajar outros membros a atingir a meta

### Busca

1. Buscar por ISBN ou Escanear Código de Barras
- **Ator Principal:** Usuário
- **Descrição:** O usuário deseja buscar um livro específico pelo seu número ISBN ou escanear o código de barras do livro para encontrar o livro exato no aplicativo e registrar seu progresso.
- **Fluxo Principal:**
    1. O usuário acessa a função de busca, que permite a busca por ISBN ou o escaneamento do código de barras, com acesso à câmera.
    2. O usuário insere manualmente o número ISBN do livro ou usa a opção de escanear o código de barras do livro.
    3. O sistema processa a entrada e localiza o livro correspondente no banco de dados.
    4. O livro correspondente é exibido com todos os detalhes relevantes, incluindo título, capa, autor e sinopse.
    5. O usuário pode selecionar o livro encontrado e registrar seu progresso de leitura.

2. Buscar por História ou Palavras-Chave
  - **Ator Principal:** Usuário
  - **Descrição:** O usuário deseja buscar livros com base na história ou em palavras-chave no aplicativo de compartilhamento de progresso de leituras. Isso permite ao usuário encontrar livros que compartilhem temas ou elementos de história específicos.
  - **Fluxo Principal:**
    1. O usuário acessa a função de pesquisa no aplicativo.
    2. O usuário insere palavras-chave, frases ou descrições de histórias que deseja encontrar em livros.
    3. O sistema processa a pesquisa e retorna uma lista de livros que correspondem às palavras-chave ou à descrição da história.
    4. Os resultados da pesquisa incluem detalhes como título, capa, autor e sinopse.
    5. O usuário pode clicar em um resultado de pesquisa para acessar mais informações sobre um livro específico e registrar seu progresso de leitura.
  - **Fluxo Alternativo:** Se não houver resultados correspondentes, o sistema informa ao usuário que a pesquisa não encontrou livros correspondentes e sugere ajustar os critérios de pesquisa.


## Estórias de usuário

### Autenticação, conta e perfil

1. Registrar conta:
  - **Descrição:** como um novo usuário que deseja usar o aplicativo, eu gostaria de criar uma nova conta para que eu possa começar a compartilhar meus progressos de leituras com amigos e acompanhar meu próprio progresso.
  - **Critérios de Aceitação:**
    - Como usuário, quero fornecer meu nome, endereço de e-mail e uma senha ao criar minha conta.
    - O sistema deve validar se o endereço de e-mail fornecido é único e se a senha atende aos requisitos de segurança.
    - Após o registro bem-sucedido, devo receber uma confirmação por e-mail para verificar meu endereço de e-mail.
2. Autenticação de Usuário
  - **Descrição:** como um usuário registrado, desejo poder entrar na minha conta para acessar todas as funcionalidades do aplicativo.
  - **Critérios de Aceitação:**
    - Como usuário registrado, quero poder fornecer meu endereço de e-mail e senha para fazer login na minha conta.
    - O sistema deve verificar se as informações de login são válidas e corresponde a uma conta registrada no sistema.
    - Após o login bem-sucedido, devo ser redirecionado para a minha página inicial do aplicativo.

### Metas de leitura individuais

1. Excluir meta de leitura individual:
  - **Descrição:** como um usuário do sistema, desejo excluir uma meta de leitura que não é mais relevante para mim e, por isso, não tenho mais interesse em cumpri-la.
  - **Critérios de aceitação:**
    - Eu quero poder excluir metas de leitura que não me interessem mais, de modo que elas não apareçam para mim da mesma forma que outras metas que ainda me interessam.
    - Eu quero que seja solicitada a minha confirmação antes da exclusão, para que não haja risco de que eu exclua alguma meta de leitura por acidente.
    - Eu quero que meus progressos de leitura relacionados a essa meta não sejam perdidos, mas sim apenas desassociados dela.
    - Eu gostaria de ser capaz de recuperar e editar essa meta de leitura caso mude de ideia e deseje retomá-la.
    - Eu gostaria de poder excluir permanentemente uma meta de leitura já movida para a seção de metas excluídas, impossibilitando sua recuperação no futuro.
    - Eu gostaria que, antes de excluir permanentemente alguma meta, o sistema peça minha confirmação e avise que não será possível reverter essa ação.

2. Visualizar histórico de metas de leitura:
  - **Descrição:** como usuário do sistema, desejo ser capaz de visualizar metas de leitura individuais que já estabeleci ao longo do meu uso do sistema e visualizar seu status (em andamento, concluída, excluída).
  - **Critérios de aceitação:**
    - Eu quero poder visualizar todo o meu histórico de metas de leituras ao longo do uso do sistema em ordem cronológica decrescente (ou seja, das mais recentes até as mais antigas).
    - Eu quero poder filtrar as metas de leitura existentes segundo o status, podendo visualizar apenas as que estão em andamento, já concluídas ou que foram excluídas.
    - Eu gostaria que as metas excluídas estivessem por padrão em uma aba separada, para que não se misturem com as metas não-excluídas, mas que também seja possível listar todas as metas (excluídas ou não) em uma mesma página.

### Metas de leitura - estendido para multiplas pessoas.

1. Criar meta privada:
  - **Descrição:** como usuário do sistema e professor eu quero criar uma meta para meus alunos lerem o livro da disciplina.
  - **Critérios de aceitação:**
    - Eu quero encontrar o livro e a versão a ser trabalhado na disciplina
    - Eu quero cadastrar o livro se ele não existir na plataforma
    - Eu quero fornecer a data limite e as páginas a serem lidas
    - Eu quero receber um codigo para passar para meus alunos
    - Eu quero que essa meta não seja visivel por terceiros e apenas quem possuir o código poder acessar-la

2. Entrar em metas aleatórias:
  - **Descrição:** como usuário e leitor eu quero me desafiar e aceitar desafios de leitura propostos por outras pessoas.
  - **Critérios de aceitação:**
    - Eu quero pesquisar por um tema que eu goste e que o sistema me liste recomendações de metas
    - Quero que seja possivel visualizar quantas pessoas estão escritas na meta sem que eu precise efetivamente entrar na meta
    - Quero desistir da meta se a narrativa do livro for ruim

### Progresso de leitura
1. Visualizar o progresso de outro usuário:
   - **Descrição:** Como um usuário do sistema, quero poder ver o progresso dos meus amigos para ver o que estão lendo.
   - **Critérios de Aceitação:**
    - Quero encontrar o nome de usuário do meu amigo na busca
    - Quero poder acessar o perfil do meu no sistema depois de encontrá-lo na busca
    - Quero poder visualizar os progressos de leitura do meu amigo no seu perfil

2. Marcar o progresso como concuído
   - **Descrição:** Como um usuário do sistema, quando eu terminar um livro quero simplismente deixá-lo concluído, sem precisar atualizar o progresso.
   - **Critérios de Aceitação:**
    - Quero poder selecionar o livro no meu perfil o qual desejo atualizar meu progresso
    - Quero poder atualizar o progresso para total e marcar o livro como concluído para que conste no meu perfil que eu terminei ele

### Busca

1. Pesquisa de Livro por Título
- **Descrição:** Como um usuário do sistema, desejo poder pesquisar livros pelo título no aplicativo de compartilhamento de progresso de leituras, para que eu possa facilmente encontrar e registrar o progresso de leitura de livros específicos.
- **Critérios de Aceitação:**
  - Quero poder procurar um livro no aplicativo
  - Quero encontrar várias opções de livros com base na minha pesquisa para poder escolher o livro que eu estou procurando.
  - Quero poder visualizar mais detalhos do livro além do seu título para ver se é o livro que estou procurando.

2. Pesquisa de Livro por Código ISBN
- **Descrição:** Tenho meus livros em casa e gostaria de adicioná-los ao meu progresso de leitura no aplicativo, não quero adicionar outro livro por engano, então quero pesquisar pelo código ISBN do meu livro para saber que vou adicionar exatamente o livro que desejo.
- **Critérios de Aceitação:**
  - Quero encontrar um livro específico pelo código do ISBN.
  - Quero visualizar os detalhes do meu livro para poder registrar meu progressor de leitura.
