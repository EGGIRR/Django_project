import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class User(AbstractUser):
    fname = models.CharField(max_length=150, verbose_name='Имя', null=False, blank=False)
    lname = models.CharField(max_length=150, verbose_name='Фамилия', null=True, blank=True)
    sname = models.CharField(max_length=150, verbose_name='Отчество', null=False, blank=False)
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True, null=False, blank=False)
    email = models.CharField(max_length=250, verbose_name='Почта', unique=True, null=False, blank=False)
    password = models.CharField(max_length=250, verbose_name='Пароль', null=False, blank=False)
    photo = models.ImageField(upload_to=get_name_file, blank=False)
    def full_name(self):
        return str(self.lname) + ' ' + str(self.fname) + ' ' + str(self.sname)

    def __str__(self):
        return self.full_name()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
