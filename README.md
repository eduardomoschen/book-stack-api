# Book Stack

O projeto Book Stack é uma API desenvolvida em Django Rest Framework que fornece serviços para gerenciar um sistema de biblioteca. A API oferece operações CRUD para entidades fundamentais, como livros, usuários e empréstimos. Além disso, integra autenticação JWT para garantir a segurança das operações.

## Recursos Adicionais

- **Autenticação JWT:** Implementação de autenticação JWT para garantir a segurança das chamadas à API.

- **Signals para Envio de E-mails:** Utilização de signals para enviar e-mails automatizados. Isso inclui lembretes com 1 dia de antecedência para devolução e notificações diárias após o vencimento.


## Experimente Localmente

1. **Clone o Repositório:**
    ```bash
    git clone git@github.com:eduardomoschen/book-stack-api.git
    ```

2. **Instale as Dependências:**
    ```bash
    cd book-stack-api
    pip install -r requirements.txt
    ```

3. **Inicie o Servidor:**
    ```bash
    python manage.py runserver
    ```

4. **Acesse o Aplicativo em [http://localhost:8000/api/v1/](http://localhost:8000/api/v1)**
    - **Criar um Livro:**
        - `POST books/` - Cria um livro informando os dados abaixo:
            - `isbn`: Campo para adicionar o ISBN do livro.
            - `title`: Campo para adicionar o título do livro.
            - `author`: Campo para adicionar o nome do autor do livro.
            - `year_of_publication`: Campo para adicionar o ano que o livro foi publicado.
            - `publisher`: Campo para adicionar o nome da editora que publicou o livro.
            - `image`: Campo para adicionar o link da imagem do livro.

    - **Listar Livros:**
        - `GET books/` - Lista todos os livros cadastrados.

    - **Detalhar um Livro:**
        - `GET book/<isbn>/` - Retorna detalhes de um livro específico com base no ISBN fornecido.

    - **Atualizar um Livro:**
        - `PATCH book/<isbn>/` - Atualiza os dados do livro de forma parcial com base no ISBN fornecido.

    - **Excluir um Livro:**
        - `DELETE book/<isbn>/` - Delete o livro com base no ISBN fornecido.

    - **Criar um Usuário:**
        - `POST users/` - Cria um usuário informando os dados abaixo:
            - `first_name`: Campo para adiconar o primeiro nome do usuário.
            - `last_name`: Campo para adicionar o último nome do usuário.
            - `username`: Campo para adicionar o username do usuário.
            - `email`: Campo para adicionar o e-mail do usuário.
            - `phone_number`: Campo para adicionar o número de telefone do usuário.
            - `password`: Campo para adicionar a senha criada pelo usuário.
            - `birth_date`: Campo para adicionar a data de nascimento do usuário.

    - **Listar Usuários:**
        - `GET users/` - Lista todos os usuários cadastrados.

    - **Detalhar um Usuário:**
        - `GET user/<username>/` - Retorna detalhes de um usuário específico com base no username fornecido.

    - **Atualizar um Usuário:**
        - `PATCH user/<username>/` - Atualiza os dados do usuário de forma parcial com base no username fornecido.

    - **Excluir um Usuário:**
        - `DELETE user/<username>/` - Deleta um usuário específico com base no username fornecido.

    - **Criar um Empréstimo:**
        - `POST borrowers/` - Cria um empréstimo informando os dados abaixo:
            - `borrower`: Campo para adicionar o ID do usuário que irá realizar o empréstimo.
            - `book`: Campo para adicionar o ID do livro que será emprestado.
            - `date_issued`: Campo para adicionar a data que está realizando o empréstimo.
            - `due_date`: Campo para adicionar a data que é para o usuário devolver o livro.

    - **Listar Empréstimos:**
        - `GET borrowers/` - Lista todos os empréstimos realizados.

    - **Detalhar um Empréstimo:**
        - `GET borrower/<id>/` - Retorna um empréstimo específico com base no ID fornecido.

    - **Atualizar um Empréstimo:**
        - `PATCH borrower/<id>/` - Atualiza dados do empréstimo com base no ID fornecido.

    - **Devolver um Livro:**
        - `PATCH borrower/<id>/` - Devolve o livro que foi emprestado ao usuário. Para isso, é necessário enviar apenas esses dados:
            - `returned`: Campo bool para confirmar que o livro foi devolvido.
            - `date_delivered`: A data que o livro foi entregue.

    - **Excluir um Empréstimo:**
        - `DELETE borrower/<id>/` - Delete um livro específico com base no ID fornecido.

    - **Obter Token de Acesso:**
        - `POST authentication/token/` - Obtém um token de acesso fornecendo credenciais válidas.

    - **Atualizar Token de Acesso:**
        - `POST authentication/token/refresh/` - Atualiza um token de acesso expirado para um novo token válido.

    - **Verificar Token de Acesso:**
        - `POST authentication/token/verify/` - Verifica se um token de acesso é válido.


## Contribua e Compartilhe

Você tem ideias para melhorar o Book Stack? Sinta-se à vontade para contribuir com novos recursos, correções ou melhorias no código. Siga estes passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição: `git checkout -b minha-contribuicao`.
3. Commit as mudanças: `git commit -m 'Adicionando recurso novo'`.
4. Faça push da sua branch: `git push origin minha-contribuicao`.
5. Crie um pull request.

## Licença

Este projeto é licenciado sob os termos da MIT License, localizado no arquivo [LICENSE](https://github.com/eduardomoschen/book-stack-api/blob/main/LICENSE) neste repositório.