from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book


User = get_user_model()


class BookBorrowing(models.Model):
    """
    Reprentação do model para o empréstimo do livro.

    Atributos:
        - book: O livro que foi emprestado.
        - borrower: O usuário que realizou o empréstimo.
        - date_issued: A data que foi realizada o empréstimo.
        - due_date: A data que deverá ser devolvido o livro.
        - returned: Campo booleano que representa a disponibilidade do livro.
        - date_delivered: A data que o livro foi entregue.

    Métodos:
        - __str__: Retorna uma representação em string do título do livro e do
        usuário que realizou o empréstimo.
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    date_delivered = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} - {self.borrower}"


class Notification(models.Model):
    """
    Representação da notificação que será enviada ao usuário a respeito das
    datas dos livros.

    Atributos:
        - user: O usuário a ser notificado.
        - message: A mensagem de acordo com a finalidade desejada.
        - created_at: O dia em que foi realizada a notificação para o usuário.
        - read: Campo booleano para informar se a mensagem foi lida ou não.

    Métodos:
        - __str__: Retorna uma representação em string informando o username e a
        mensagem enviada.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.message}'
