from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    time_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



