from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieModel
# from rest_framework.permissions import IsAuthenticated

# create a viewset
# class MovieViewSet(viewsets.ReadOnlyModelViewSet):
class MovieViewSet(viewsets.ModelViewSet):
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer