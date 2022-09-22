from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        fields = '__all__'
        model = Snippet