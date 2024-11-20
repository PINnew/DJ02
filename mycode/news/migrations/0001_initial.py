# Generated by Django 5.1.3 on 2024-11-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название новости')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание новости')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('text', models.TextField(max_length=200, verbose_name='Новость')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]