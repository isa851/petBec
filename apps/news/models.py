from django.db import models

class NewsTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="news/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
