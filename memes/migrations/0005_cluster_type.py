# Generated by Django 2.1.3 on 2018-11-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0004_auto_20181110_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='type',
            field=models.CharField(max_length=2048, null=True, verbose_name='type'),
        ),
    ]