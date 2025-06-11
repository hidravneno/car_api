from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Car
from .serializers import CarSerializer
from .permissions import IsOwnerOrReadOnly

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    queryset = Car.objects.all()  # <--- Aquí

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
