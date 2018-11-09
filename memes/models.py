from django.db import models
import datetime

# Create your models here.

class Cluster(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано',
        default=timezone.now
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=2048
    )

class Keywords(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано',
        default=timezone.now
    )
    word = models.CharField(
        verbose_name='Ключевое слово',
        max_length=64
    )
    cluster_id = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING)

    weight = models.FloatField(
        verbose_name='Вес',
        null=True
    )

class Meme(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано',
        default=timezone.now
    )
    image_url = models.CharField(
        verbose_name='Путь к изображению',
        max_length=2048
    )
    raw_text = models.CharField(
        verbose_name='Текст',
        max_length=2048,
        blank=True,
        null=True
    )
    ru_text = models.CharField(
        verbose_name='Русский текст',
        max_length=2048,
        blank=True,
        null=True
    )
    en_text = models.CharField(
        verbose_name='Английский текст',
        max_length=2048,
        blank=True,
        null=True
    )
    lem_text = models.CharField(
        verbose_name='Лемматизированный текст',
        max_length=2048,
        blank=True,
        null=True
    )
    labels = models.CharField(
        verbose_name='Сущности на фото',
        max_length=2048,
        blank=True,
        null=True
    )
    cluster_text = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING)
    cluster_label = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING)



