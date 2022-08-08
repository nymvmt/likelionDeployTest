from django.db import models
from django.contrib.auth.models import User
#User model https://docs.djangoproject.com/en/4.0/ref/contrib/auth/


# Create your models here.
class Profile(User):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profiles')
  nickname = models.CharField(max_length = 50)

  def __str__(self):
    return self.username