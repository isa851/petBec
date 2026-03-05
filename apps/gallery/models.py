from django.db import models

class GalleryTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"

class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"