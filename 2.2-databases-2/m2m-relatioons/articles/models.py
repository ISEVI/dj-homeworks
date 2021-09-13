from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.TextField(max_length=256, verbose_name='Название')
    articles = models.ManyToManyField(Article, through='ArticleScope')

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'CтатьиТеги'
        verbose_name_plural = 'CтатьиТеги'

    def __str__(self):
        return f"{self.article} : {self.scope} : {self.is_main}"
