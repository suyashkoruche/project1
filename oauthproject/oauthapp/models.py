from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Snippet(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippet', null=True, blank=True)
