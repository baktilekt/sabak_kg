# Generated by Django 4.0.1 on 2022-02-07 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_alter_lesson_home_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='lessons.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано?'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео'),
        ),
    ]
