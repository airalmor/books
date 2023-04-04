import django_filters
from django.shortcuts import render

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from store.models import Book, UserBookRelation
from store.permissions import IsOwnerOrStaffOrReadOnly
from store.serializers import BooksSerializer, UserBookRelationSerializer


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filterset_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_filter = ['price', 'author_name']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserBookRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = 'book'

    def get_object(self):
        obj, _=UserBookRelation.objects.get_or_create(user=self.request.user,
                                                      book_id=self.kwargs['book'])
        return obj


def auth(request):
    return render(request, 'oauth.html')
