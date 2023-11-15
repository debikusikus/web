from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class comment(models.Model):
    author = models.CharField(max_length=50, help_text='Автор комментария, ограниченный 50 символами')
    text = models.TextField(help_text='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Дата и время создания комментария')
    updated_at = models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления комментария')
class tag(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='Имя тега, ограниченное 50 символами')
    description = models.TextField(blank=True, null=True, help_text='Описание тега')
class category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Название категории, ограниченный 100 символами')
    description = models.TextField(blank=True, null=True, help_text='Описание категории')