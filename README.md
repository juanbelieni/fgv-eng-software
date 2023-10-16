# Projeto de Engenharia de Software

## Metáfora do sistema

...

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
