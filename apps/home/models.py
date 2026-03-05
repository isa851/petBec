from django.db import models

class HomeTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заголовок страницы"
        verbose_name_plural = "Заголовки страниц"
        
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class OurSuccess(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наш успех"
        verbose_name_plural = "Наши успехи"

class LatestNews(models.Model):
    images = models.ImageField(upload_to='latest_news/')
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Последняя новость"
        verbose_name_plural = "Последние новости"

class HowItWorks(models.Model):
    icon = models.ImageField(upload_to='how_it_works/')
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Как это работает"
        verbose_name_plural = "Как это работает"


class NeedSupport(models.Model):    
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    yourQuery = models.TextField(verbose_name="Ваш запрос")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нужна поддержка"
        verbose_name_plural = "Нужна поддержка"
