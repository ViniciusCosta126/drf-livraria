# Generated by Django 4.2.7 on 2023-11-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_alter_livro_sinopse_alter_livro_thumb_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='categorias',
            field=models.ManyToManyField(related_name='categorias', to='livraria.categoria'),
        ),
    ]
