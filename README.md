# Projeto de Engenharia de Software

## Metáfora do sistema

Imaginemos o sistema como uma biblioteca univercitária que tenha salas de estudo, individuais e em grupo.

  1. Autenticação de usuário:
    Cada usuário possui seu identificador na biblioteca, um crachá, o qual permite que ele entre na biblioteca, esse seria o 'username' de cada usuário no sistema.
  2. Pesquisar livro:
    Seria como perguntar para a bibliotecaria onde fica tal livro e ela te mostraria as opções de acordo com sua descrição.
  3. Gerar meta de leitura:
    Seria análogo a reservar uma sala de estudos por um determinado tempo para ler um livro ou partes de um livro em específico, nesse momento a pessoa que reservou a sala se tornaria responsável(adiministradora ou editora) pela sala.
      - Gerar meta de leitura publica: reservar a sala e avisar à recepção que qualquer um pode participar dessa sala.
  4. Entrar em uma meta de leitura:
    Ao ser Convidado por um responsável pela sala o usuário pode se registrar para frequentar uma sala e se propor a cumprir a meta daquela sala.
      - Entrar em uma meta publica: pedir para a recepção as salas com atividades publicas e fazer o registo para participar da atividade da sala.
  5. Atualizar o progresso de leitura:
    O usuário assim que pausa sua leitura escreve num canto do quadro branco da sala a página onde parou.


## Casos de uso

### Autenticação, conta e perfil

1. Atualização do Perfil do Usuário
  - Atores: usuário registrado e sistema.
  - Descrição: o usuário deseja poder atualizar as informações do seu perfil.
  - Fluxo Principal:
    1. O usuário faz login na sua conta.
    2. O usuário navega até a seção de "Perfil" do aplicativo.
    3. O usuário pode editar informações como nome, foto de perfil e outras informações relevantes.
    4. O usuário salva as alterações no seu perfil.
2. Recuperação de Senha
  - Atores: usuário registrado e sistema.
  - Descrição: o usuário esqueceu sua senha e deseja redefini-la de forma segura.
  - Fluxo Principal:
    1. O usuário acessa a tela de login do aplicativo.
    2. O usuário clica na opção "Esqueci minha senha".
    3. O sistema solicita o endereço de e-mail do usuário.
    4. O sistema envia um e-mail de redefinição de senha para o endereço de e-mail fornecido.
    5. O usuário verifica seu e-mail e clica no link de redefinição de senha.
    6. O sistema permite que o usuário defina uma nova senha.
    7. O sistema confirma a alteração da senha e redireciona o usuário para a tela de login, onde ele pode acessar sua conta com a nova senha.

### Metas de leitura - estendido para multiplas pessoas.

1. Entrar em uma meta existente:
  - Atores: Usuario e sistema
  - Descrição: O usuário deseja deseja entrar em uma meta de leitura já estabelecida por alguém.
  - Fluxo Principal:
    1. O usuário faz login à sua conta
    2. O usuário navega até a sessão de metas
    3. O entra em adicionar nova meta e vai em embarcar em meta existente e coloca o codigo que recebeu de algum amigo
    4. O sistema recebe o codigo busca no banco de dados e cadatra ele naquela meta

2. Criar uma meta publica:
  - Atores: Usuário e sistema
  - Descrição: O usuário deseja criar uma meta publica
  - Fluxo Principal:
    1. O usuário faz login
    2. Navega até a sessão metas
    3. Entra em adicionar nova meta e vai em criar nova meta
    4. seleciona o livro desejado, com opção de livro completo, adiciona a data limite e informa que a meta é publica e a nomeia
    5. o sistema recebe as informações acima e cria a meta com o usuario como editor e coloca ela na lista de metas publicas para ser visualisada por todos que assim quiserem.

### Busca

1. Buscar por ISBN ou Escanear Código de Barras
  - Ator Principal: Usuário
  - Descrição: O usuário deseja buscar um livro específico pelo seu número ISBN ou escanear o código de barras do livro para encontrar o livro exato no aplicativo e registrar seu progresso.
  - Fluxo Principal:
    1. O usuário acessa a função de busca, que permite a busca por ISBN ou o escaneamento do código de barras, com acesso à câmera.
    2. O usuário insere manualmente o número ISBN do livro ou usa a opção de escanear o código de barras do livro.
    3. O sistema processa a entrada e localiza o livro correspondente no banco de dados.
    4. O livro correspondente é exibido com todos os detalhes relevantes, incluindo título, capa, autor e sinopse.
    5. O usuário pode selecionar o livro encontrado e registrar seu progresso de leitura.

2. Buscar por História ou Palavras-Chave
  - Ator Principal: Usuário
  - Descrição: O usuário deseja buscar livros com base na história ou em palavras-chave no aplicativo de compartilhamento de progresso de leituras. Isso permite ao usuário encontrar livros que compartilhem temas ou elementos de história específicos.
  - Fluxo Principal:
    1. O usuário acessa a função de pesquisa no aplicativo.
    2. O usuário insere palavras-chave, frases ou descrições de histórias que deseja encontrar em livros.
    3. O sistema processa a pesquisa e retorna uma lista de livros que correspondem às palavras-chave ou à descrição da história.
    4. Os resultados da pesquisa incluem detalhes como título, capa, autor e sinopse.
    5. O usuário pode clicar em um resultado de pesquisa para acessar mais informações sobre um livro específico e registrar seu progresso de leitura.
  - Fluxo Alternativo: Se não houver resultados correspondentes, o sistema informa ao usuário que a pesquisa não encontrou livros correspondentes e sugere ajustar os critérios de pesquisa.


## Estórias de usuário

### Autenticação, conta e perfil

1. Registrar conta:
  - Descrição: como um novo usuário que deseja usar o aplicativo, eu gostaria de criar uma nova conta para que eu possa começar a compartilhar meus progressos de leituras com amigos e acompanhar meu próprio progresso.
  - Critérios de Aceitação:
    - Como usuário, quero fornecer meu nome, endereço de e-mail e uma senha ao criar minha conta.
    - O sistema deve validar se o endereço de e-mail fornecido é único e se a senha atende aos requisitos de segurança.
    - Após o registro bem-sucedido, devo receber uma confirmação por e-mail para verificar meu endereço de e-mail.
2. Autenticação de Usuário
  - Descrição: como um usuário registrado, desejo poder entrar na minha conta para acessar todas as funcionalidades do aplicativo.
  - Critérios de Aceitação:
    - Como usuário registrado, quero poder fornecer meu endereço de e-mail e senha para fazer login na minha conta.
    - O sistema deve verificar se as informações de login são válidas e corresponde a uma conta registrada no sistema.
    - Após o login bem-sucedido, devo ser redirecionado para a minha página inicial do aplicativo.

### Metas de leitura - estendido para multiplas pessoas.

1. Criar meta privada:
  - Descrição: como usuário do sistema e professor eu quero criar uma meta para meus alunos lerem o livro da disciplina.
  - Critérios de aceitação:
    - Eu quero encontrar o livro e a versão a ser trabalhado na disciplina
    - Eu quero cadastrar o livro se ele não existir na plataforma
    - Eu quero fornecer a data limite e as páginas a serem lidas
    - Eu quero receber um codigo para passar para meus alunos
    - Eu quero que essa meta não seja visivel por terceiros e apenas quem possuir o código poder acessar-la

2. Entrar em metas aleatórias:
  - Descrição: como usuário e leitor eu quero me desafiar e aceitar desafios de leitura propostos por outras pessoas.
  - Critérios de aceitação:
    - Eu quero pesquisar por um tema que eu goste e que o sisteme me liste recomendações de metas
    - Quero que seja possivel visualizar quantas pessoas estão escritas na meta sem que eu precise efetivamente entrar na meta
    - Quero desistir da meta se a narrativa do livro for ruim

### Busca

1. Pesquisa de Livro por Título
  - Descrição: Como um usuário ávido leitor, desejo poder pesquisar livros pelo título no aplicativo de compartilhamento de progresso de leituras, para que eu possa facilmente encontrar e registrar o progresso de leitura de livros específicos.
  - Critérios de Aceitação:
    - No aplicativo, existe uma barra de pesquisa que permite aos usuários inserir o título do livro desejado.
    - O sistema deve fornecer resultados relevantes que correspondam ao título inserido.
    - Os resultados da pesquisa devem incluir o título do livro, a capa, o autor e outros detalhes relevantes.
    - Os resultados da pesquisa devem ser apresentados de forma clara e organizada para facilitar a seleção do livro desejado.
    - Os usuários podem clicar em um resultado de pesquisa para visualizar detalhes adicionais e registrar seu progresso de leitura nesse livro.

2. Pesquisa de Livro por Autor
  - Descrição: Como um entusiasta da literatura e fã de certos autores, desejo poder pesquisar livros pelo autor de meu interesse no aplicativo de compartilhamento de progresso de leituras.
  - Critérios de Aceitação:
    - No aplicativo, há a de pesquisa, onde é possível que os usuários insiram o nome do autor desejado.
    - O sistema deve fornecer resultados que correspondam ao autor inserido.
    - Os resultados da pesquisa por autor devem incluir uma lista de livros escritos por esse autor, juntamente com detalhes como título, capa e outros detalhes relevantes.
    - Os resultados da pesquisa por autor devem ser apresentados de forma organizada e de fácil leitura.
    - Os usuários podem clicar em um resultado de pesquisa para visualizar detalhes adicionais e registrar seu progresso de leitura em um livro específico do autor.
