from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class YearField(models.IntegerField):
    """
    Um campo de model personalizado para representar um ano.

    Este campo herda da classe IntegerField e adiciona validadores para
    garantir que o valor esteja dentro de um intervalo específico.

    Atributos:
        - *args, **kwargs: Argumentos adicionais que podem ser passados para o
        construtor.

    Métodos:
        __init__: Inicializa o campo YearField.
    """

    def __init__(self, *args, **kwargs):
        """
        Inicializa o campo YearField.

        Parâmetros:
            - *args, **kwargs: Argumentos adicionais para serem passados para o
            construtor da classe pai (IntegerField).

        Comportamento:
            Define validadores para garantir que o valor do ano esteja entre
            1500 e o ano atual. Além diso, adiciona uma mensagem de ajuda para
            orientar os usuários a inserirem um ano no formato (YYYY).
        """

        current_year = datetime.date.today().year
        kwargs['validators'] = [
            MinValueValidator(1500),
            MaxValueValidator(current_year)
        ]
        kwargs['help_text'] = "Digite um ano (YYYY)"
        super().__init__(*args, **kwargs)

class Book(models.Model):
    """
    Representação do livro.

    Atributos:
        - isbn: O número do ISBN do livro.
        - title: O título do livro.
        - author: O autor do livro.
        - year_of_publication: O ano de publicação do livro.
        - publisher: A editora do livro.
        - image: URL da imagem da capa do livro.
        - available: Indica se o livro está disponível para empréstimo.
        - waiting_list: Lista de usuários em lista de espera para o livro.

    Métodos:
        __str__: Retorna uma representação em string do nome do livro.
    """

    isbn = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    year_of_publication = YearField()
    publisher = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField()
    available = models.BooleanField(default=True)
    waiting_list = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
