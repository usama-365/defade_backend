from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255)
    result = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)