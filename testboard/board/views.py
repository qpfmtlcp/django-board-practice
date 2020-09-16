from rest_framework import generics
from .serializer import BoardSerializer, UserSerializer
from django_filters import rest_framework as filters
from .models import Board, User


class BoardFilter(filters.FilterSet):
    class Meta:
        model = Board
        fields = ['status']
        
class BoardView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filterset_class= BoardFilter
    
class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer