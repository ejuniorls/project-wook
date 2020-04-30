from django.db import models

# Create your models here.

class CountryManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(code__icontains=query)
        )

class Country(models.Model):
    name = models.CharField('País', max_length=50, unique=True)
    code = models.CharField('Sigla', max_length=3, unique=True)
    slug = models.SlugField('pais', unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CountryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Countries'
        ordering = ['name']

class Genre(models.Model):
    name = models.CharField('Gênero', max_length=20)
    slug = models.SlugField('genero')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField('Editora', max_length=20)
    slug = models.SlugField('editora')
    page = models.CharField('Site', max_length=20)
    logo = models.ImageField(upload_to='publisher/images', verbose_name='Imagem')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

class AuthorManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(first_name__icontains=query) | \
            models.Q(last_name__icontains=query) | \
            models.Q(location__icontains=query) | \
            models.Q(popular_name__icontains=query)
        )

class Author(models.Model):
    first_name = models.CharField('Nome', max_length=30, blank=False)
    last_name = models.CharField('Sobrenome', max_length=50, blank=False)
    popular_name = models.CharField('Nome popular', max_length=30, blank=False)
    slug = models.SlugField('nome', blank=False)
    birth =  models.DateField('Nascimento', blank=True)
    death =  models.DateField('Falecimento', blank=True)
    location = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='author/images', verbose_name='Imagem', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AuthorManager()

    def __str__(self):
        return self.popular_name

    class Meta:
        verbose_name_plural = 'Authors'

class BookManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(title_pt__icontains=query) | \
            models.Q(title_original__icontains=query) | \
            models.Q(author__icontains=query) | \
            models.Q(year__icontains=query) | \
            models.Q(publisher__icontains=query) | \
            models.Q(isbn10__icontains=query) | \
            models.Q(isbn13__icontains=query) | \
            models.Q(cdu__icontains=query) | \
            models.Q(cdd__icontains=query)
        )

class Book(models.Model):
    title_pt = models.CharField('Título PT', max_length=50, blank=False)
    title_original = models.CharField('Título original', max_length=50, blank=False)
    slug = models.CharField('titulo', max_length=50, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)
    year = models.IntegerField('Ano', blank=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=False)
    pages = models.IntegerField('Páginas', blank=False)
    isbn10 = models.CharField('ISBN 10', max_length=10, blank=True)
    isbn13 = models.CharField('ISBN 13', max_length=13, blank=True)
    cdd = models.CharField('CDD', max_length=10, blank=True)
    cdu = models.CharField('CDU', max_length=10, blank=True)
    summary = models.TextField(blank=False)
    cover = models.ImageField(upload_to='cover/images', verbose_name='Imagem', blank=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = BookManager()

    def __str__(self):
        return self.title_pt

    class Meta:
        verbose_name_plural = 'Books'

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.book.title_pt

    class Meta:
        verbose_name_plural = 'Books Genre'

class BookRate(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False)
    rate = models.FloatField('Rate', blank=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.book.title_pt

    class Meta:
        verbose_name_plural = 'Books Rate'
