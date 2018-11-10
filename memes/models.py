from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

@property
def clear(self):
    return self.replace('memes2k18','')

class Cluster(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано',
        default=timezone.now
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=2048
    )
    requests = models.IntegerField(
        verbose_name='Количество запросов за последние 24 часа',
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
        max_length=16348,
        blank=True,
        null=True
    )
    ru_text = models.CharField(
        verbose_name='Русский текст',
        max_length=16438,
        blank=True,
        null=True
    )
    en_text = models.CharField(
        verbose_name='Английский текст',
        max_length=16348,
        blank=True,
        null=True
    )
    lem_text = models.CharField(
        verbose_name='Лемматизированный текст',
        max_length=16348,
        blank=True,
        null=True
    )
    labels = models.CharField(
        verbose_name='Сущности на фото',
        max_length=16384,
        blank=True,
        null=True
    )
    cluster_text = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING, related_name='cluster_text', null=True)
    cluster_label = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING, related_name='cluster_label', null=True)


