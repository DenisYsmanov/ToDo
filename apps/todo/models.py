from django.db import models


class Todo(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название задания',
        default='Default Title',
    )
    text = models.TextField(
        verbose_name='Задание',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создание',
    )
    is_complete = models.BooleanField('Завершено',default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= 'Задание'
        verbose_name_plural = 'Задания'