# Generated by Django 3.2 on 2021-04-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_actor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor', verbose_name='Actores'),
        ),
    ]
