from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication
from .permissions import UserIsAuthenticatedorReadOnly, UserIsAdminUser, IsOwnerorReadOnly

# Create your views here.


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = [UserIsAdminUser]
    authentication_classes = [IsOwnerorReadOnly]

