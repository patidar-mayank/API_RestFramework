from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer  # Corrected attribute name

# Create your views here.
