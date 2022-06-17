# Generated by Django 4.0.3 on 2022-05-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Manzil')),
            ],
            options={
                'verbose_name': 'Category_blog',
                'verbose_name_plural': 'Categories_blog',
            },
        ),
    ]
