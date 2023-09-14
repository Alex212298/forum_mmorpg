from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
     post_id = models.BigAutoField(primary_key=True, unique=True)
     heading = models.CharField(max_length=128, verbose_name='Заголовок')
     DD = 'DD'
     TANK = 'TT'
     HIL = 'HIL'
     TRADER = 'TRADER'
     GILDMASTER = 'GM'
     QUESTGIVER = 'QG'
     FARRIER = 'FARRIER'
     TANNER = 'TANNER'
     ALCHEMIST = 'ALCHEMIST'
     MAG = 'MAG'
     CATEGORY = [
          (DD, 'ДД'),
          (TANK, 'Танк'),
          (HIL, 'Хил'),
          (TRADER, 'Торговец'),
          (GILDMASTER, 'Гильдмастер'),
          (QUESTGIVER, 'Квестгивер'),
          (FARRIER, 'Кузнец'),
          (TANNER, 'Кожевник'),
          (ALCHEMIST, 'Алхимик'),
          (MAG, 'Мастер заклинаний'),
     ]

     category = models.CharField(
          choices=CATEGORY,
          default=DD,
          max_length=50,
          verbose_name='Категория',
     )
     content = models.FileField(blank=True, upload_to="content/%Y/%m/%d/", verbose_name='Загрузить файл')
     text = models.TextField(verbose_name='Текст')
     data_create = models.DateTimeField(auto_now_add=True)
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          return self.heading

class Repsponses(models.Model):
     resp_id = models.BigAutoField(primary_key=True, unique=True)
     resp_text = models.TextField(blank=True, max_length=255, verbose_name='Текст')
     user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
     post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Пост')


     def __str__(self):
          return self.resp_id