
# Create your models here.
from django.db import models

# Модель Post представляет одну запись блога
class Post(models.Model):
    # Заголовок статьи, ограничен 200 символами
    title = models.CharField(max_length=200)

    # Содержимое статьи — текст произвольной длины
    content = models.TextField()

    # Дата и время создания статьи, устанавливается автоматически при создании
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод отображения объекта в админке и других местах
    def __str__(self):
        return self.title
