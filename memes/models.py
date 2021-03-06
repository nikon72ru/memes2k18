from django.db import models
import datetime
from django.utils import timezone
from django.utils.safestring import mark_safe

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
    requests = models.IntegerField(
        verbose_name='Количество запросов за последние 24 часа',
    )
    type = models.CharField(
        verbose_name = 'type',
        max_length=2048,
        null=True
    )

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=2048,
        null = True
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=4096,
        null = True
    )

    def previews(self):
        str = ""
        for img in Meme.objects.filter(cluster_label=self)[:8]:
            str = str + '<img src="%s" style="width: auto; height:100px; margin:2px;" />' % img.image_url
        return mark_safe(str)

    previews.allow_tags = True

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


