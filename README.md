# Projeto de Engenharia de Software

## Metáfora do sistema

...

## Casos de uso

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


## Estórias de usuário


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
