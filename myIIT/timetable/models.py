from django.db import models
from django.contrib.auth.models import Group


class Lecturer(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=64, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=64, blank=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=64, blank=True)
    contact = models.CharField(verbose_name='Контакт', max_length=256, blank=True)

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'

    def __str__(self):
        return self.get_lecture_name()

    def get_lecture_name(self):
        lecture_name = '%s %s.%s.' % (self.last_name, self.first_name[0], self.patronymic[0])
        return lecture_name.strip()

    def get_lecture(self):
        if len(self.position) > 0:
            return '%s %s' % (self.position, self.get_lecture_name())
        return self.get_lecture_name()


class ClassCabinet(models.Model):

    title = models.CharField(verbose_name='Номер кабинета', max_length=4, blank=True)
    building = models.IntegerField(verbose_name='Корпус', default=1)

    class Meta:
        verbose_name = 'кабинет'
        verbose_name_plural = 'кабинеты'

    def __str__(self):
        if self.building > 1:
            return '%dК. Ауд. %s' % (self.building, self.title)
        return 'Ауд. %s' % self.title


class TimeSchedule(models.Model):
    number = models.IntegerField(verbose_name='Номер пары', default=0, unique=True)
    start_time = models.CharField(verbose_name='Время начала', max_length=5, unique=True)
    end_time = models.CharField(verbose_name='Время окончания', max_length=5, unique=True)

    class Meta:
        verbose_name = 'время занятия'
        verbose_name_plural = 'время занятий'

    def __str__(self):
        return '%d. %s' % (self.number, self.get_time())

    def get_time(self):
        return '%s-%s' % (self.start_time, self.end_time)


class Subject(models.Model):
    CHOICES = (
        ('UN', 'Неизвестно'),
        ('LE', 'Лекция'),
        ('PR', 'Практика'),
    )
    title = models.CharField(verbose_name='Предмет', max_length=256, blank=True)
    type = models.CharField(verbose_name='Тип пары', choices=CHOICES, max_length=2, default='LE')

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):
        if not self.type == 'UN':
            return '%s (%s.)' % (self.title, self.get_type_display()[:3])
        return self.title


class LessonSchedule(models.Model):
    CHOICES_WEEK = (
        ('MO', 'Понедельник'),
        ('TU', 'Вторник'),
        ('WE', 'Среда'),
        ('TH', 'Четверг'),
        ('FR', 'Пятница'),
        ('SA', 'Суббота'),
        ('SU', 'Воскресение'),
    )

    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, verbose_name='Группы')
    number_week = models.IntegerField(verbose_name='Номер недели')
    lecture = models.ForeignKey(Lecturer, verbose_name='Преподаватель', on_delete=models.SET_NULL, null=True)
    cabinet = models.ForeignKey(ClassCabinet, verbose_name='Кабинет', on_delete=models.SET_NULL, null=True)
    day_week = models.CharField(verbose_name='День недели', choices=CHOICES_WEEK, max_length=2)
    time = models.ForeignKey(TimeSchedule, verbose_name='Номер пары', on_delete=models.SET_NULL, null=True)
    start_week = models.IntegerField(verbose_name='Начало недели', default=0)
    end_week = models.IntegerField(verbose_name='Конец недели', default=0)

    class Meta:
        verbose_name = 'занятие'
        verbose_name_plural = 'занятия'

    def __str__(self):
        return self.subject.title

    def get_day_week(self):
        for idx, val in enumerate(self.CHOICES_WEEK):
            if val[0] == self.day_week:
                return idx + 1
