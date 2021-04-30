from django.db import models


class Actor(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=50,
        unique=True,
    )
    age = models.PositiveIntegerField(
        verbose_name='Edad',
    )

    class Meta:
        app_label = 'movies'
        db_table = 'actor'
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=50
    )
    released = models.DateField(
        verbose_name='Año de lanzamiento'
    )
    actors = models.ManyToManyField(
        Actor,
        verbose_name='Actores',
        related_name='movies',
    )
    poster = models.ImageField(
        verbose_name='Portada',
        upload_to='movies',
        null=True,
    )

    class Meta:
        app_label = 'movies'
        db_table = 'pelicula'
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

    def __str__(self):
        return self.name


class MovieImages(models.Model):
    movie = models.ForeignKey(
        Movie,
        verbose_name='Pelicula',
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to='details',
    )

    class Meta:
        app_label = 'movies'
        db_table = 'imagenes'
        verbose_name = 'Imagenes de la pelicula'
        verbose_name_plural = None
