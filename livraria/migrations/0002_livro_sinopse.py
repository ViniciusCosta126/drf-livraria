# Generated by Django 4.2.7 on 2023-11-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
