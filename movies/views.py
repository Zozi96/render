from django.shortcuts import get_object_or_404
from django_renderpdf.views import PDFView

from .models import Movie


class MovieView(PDFView):
    template_name = 'movies/pdf.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MovieView, self).get_context_data(*args, **kwargs)
        movie = get_object_or_404(Movie, pk=self.kwargs['pk'])
        files = self.request.build_absolute_uri
        context['movie'] = movie
        context['title'] = f'Pelicula: {movie.name}'
        context['poster'] = files(f'/media/{movie.poster}')
        context['images'] = [files(f'/media/{i}') for i in movie.images.image.all]
        return context
