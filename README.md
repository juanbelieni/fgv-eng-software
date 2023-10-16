# Projeto de Engenharia de Software

## Metáfora do sistema

Imaginemos o sistema como uma biblioteca univercitária que tenha salas de estudo, individuais e em grupo.

  1. Autenticação de usuário:
    Cada usuário possui seu identificador na biblioteca, um crachá, o qual permite que ele entre na biblioteca, esse seria o 'username' de cada usuário no sistema.
  2. Pesquisar livro:
    Seria como perguntar para a bibliotecaria onde fica tal livro e ela te mostraria as opções de acordo com sua descrição.
  3. Gerar meta de leitura:
    Seria análogo a reservar uma sala de estudos por um determinado tempo para ler um livro ou partes de um livro em específico, nesse momento a pessoa que reservou a sala se tornaria responsável(adiministradora ou editora) pela sala.
      3.1. Gerar meta de leitura publica: reservar a sala e avisar à recepção que qualquer um pode participar dessa sala.
  4. Entrar em uma meta de leitura:
    Ao ser Convidado por um responsável pela sala o usuário pode se registrar para frequentar uma sala e se propor a cumprir a meta daquela sala.
      4.1. Entrar em uma meta publica: pedir para a recepção as salas com atividades publicas e fazer o registo para participar da atividade da sala.
  6. Atualizar o progresso de leitura:
    O usuário assim que pausa sua leitura escreve num canto do quadro branco da sala a página onde parou.
      
     

...

## Casos de uso

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
...

## Estórias de usuário

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

