# Generated by Django 2.0.1 on 2018-05-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20180507_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(max_length=500, upload_to='media/video/%Y/%m', verbose_name='资源文件'),
        ),
    ]
