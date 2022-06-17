# Generated by Django 4.0.3 on 2022-05-31 10:45

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(verbose_name='Kichik matn'),
        ),
    ]