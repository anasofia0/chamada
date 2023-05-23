# Registro de Presenças em Aulas - Documentação do Projeto

Este é o README do projeto "Registro de Presenças em Aulas" desenvolvido utilizando Python Flask. Esta aplicação permite que alunos de uma universidade registrem suas presenças nas aulas.

## Descrição da Aplicação

### Perfis de Usuário

A aplicação possui dois perfis de usuário:

1. Aluno: Os alunos têm acesso à funcionalidade de registrar sua presença em aulas. Eles podem visualizar as aulas disponíveis, marcar sua presença e verificar seu histórico de presenças.

2. Administrador: Os administradores têm acesso a recursos adicionais. Além das funcionalidades disponíveis para os alunos, eles também podem gerenciar as aulas, adicionar/editar/excluir aulas do sistema e visualizar o registro de presenças de todos os alunos.

### Fluxos e Funcionalidades Disponíveis

Os fluxos e funcionalidades disponíveis na aplicação são os seguintes:

1. Página de Login: Os usuários devem fazer login antes de acessar as funcionalidades da aplicação. Os alunos e administradores têm páginas de login separadas.

2. Página de Registro de Presença: Após o login, os alunos têm acesso a uma página onde podem visualizar as aulas disponíveis e registrar sua presença nas aulas desejadas.

3. Página de Histórico de Presenças: Os alunos podem visualizar seu histórico de presenças, incluindo as aulas em que marcaram presença e as datas correspondentes.

4. Página de Gerenciamento de Aulas (apenas para administradores): Os administradores têm acesso a uma página onde podem adicionar, editar e excluir aulas do sistema. Eles também podem visualizar o registro de presenças de todos os alunos.

### Principais Decisões de Projeto

- Linguagem de Programação: A aplicação foi desenvolvida em Python, utilizando o framework Flask, devido à sua simplicidade e facilidade de uso para projetos web.

- Banco de Dados: Foi utilizado um banco de dados relacional (por exemplo, MySQL, PostgreSQL) para persistir as informações das aulas, alunos e registro de presenças. A escolha do banco de dados específico depende das preferências e requisitos do ambiente de execução.

- Autenticação: Para autenticação de usuários, foi implementado um sistema de login com autenticação baseada em sessões. Senhas dos usuários são armazenadas de forma segura utilizando técnicas de criptografia.

- Interface de Usuário: A interface de usuário foi projetada de forma intuitiva e responsiva, utilizando HTML, CSS e Bootstrap para garantir uma experiência de usuário agradável em diferentes dispositivos.

## Screenshots

A seguir estão alguns screenshots das principais telas da aplicação:

![Página de Login](screenshots/login.png)

![Página de Registro de Presença](screenshots/registro_presenca.png)

![Página de Histórico de Presenças](screenshots/historico_presencas.png)

![Página de Gerenciamento de Aulas](screenshots/gerenciamento_aulas.png)

## Instruções para Executar o Projeto

Siga as instruções abaixo para executar a aplicação em um sistema limpo:

1. Certifique-se de ter o Python instalado em seu sistema. Recomenda-se a versão Python 3.7 ou superior.

2. Instale o gerenciador de dependências Poetry. Você pode encontrar instruções de instalação em https://python-poetry.org/docs/#installation.

3. Faça o download ou clone este repositório para o seu sistema.

4. No diretório raiz do projeto, execute o seguinte comando para instalar as dependências:

   ```
   poetry install
   ```

5. Após a conclusão da instalação das dependências, ative o ambiente virtual criado pelo Poetry:

   ```
   poetry shell
   ```

6. Execute o seguinte comando para iniciar a aplicação:

   ```
   python run.py
   ```

7. A aplicação estará disponível em http://localhost:5000.

Certifique-se de que as portas necessárias estejam liberadas e que não haja conflitos com outros serviços em execução.

Nota: Lembre-se de configurar corretamente as informações de conexão com o banco de dados no arquivo de configuração do projeto, caso seja necessário.

## Conclusão

Este README fornece uma visão geral do projeto "Registro de Presenças em Aulas" desenvolvido utilizando Python Flask. Descreve os perfis de usuário, fluxos e funcionalidades disponíveis, principais decisões de projeto, além de fornecer instruções para executar o projeto a partir de um sistema limpo.
