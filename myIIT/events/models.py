from django.db import models
from authentication.models import User


class Event(models.Model):
    CHOICES = (
        ('W', 'Ожидание публикации'),
        ('P', 'Опубликовано'),
        ('R', 'Отклонено'),
        ('C', 'Завершено')
    )
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.CharField(verbose_name='Описание', max_length=256)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, related_name='event')
    votes = models.ManyToManyField(User, verbose_name='Проголосовавшие', blank=True, related_name='event_votes')
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    status = models.CharField(verbose_name='Статус', max_length=2, choices=CHOICES, default='W')
    report = models.CharField(verbose_name='Сообщение', max_length=256, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'
