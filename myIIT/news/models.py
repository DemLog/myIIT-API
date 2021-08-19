from django.db import models


class CategoryArticle(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=31)
    slug = models.SlugField(verbose_name='Имя Slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    category = models.ForeignKey(CategoryArticle, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=63)
    text = models.TextField(verbose_name='Текст')
    # photo = models.ImageField(verbose_name='Фото')
    date_published = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Отложенная публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Статья'
        verbose_name_plural = 'Новости'
