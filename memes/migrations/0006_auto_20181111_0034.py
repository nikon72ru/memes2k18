# Generated by Django 2.0.2 on 2018-11-11 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0005_cluster_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='description',
            field=models.CharField(max_length=4096, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='title',
            field=models.CharField(max_length=2048, null=True, verbose_name='Заголовок'),
        ),
    ]
