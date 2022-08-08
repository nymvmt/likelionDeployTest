from datetime import date
from django.contrib.auth.models import User
from django.db import models
from accounts.models import Profile

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 200)
  content = models.TextField()
  image = models.ImageField(upload_to="", blank=True)
  # create_dt = models.DateTimeField(auto_now_add = True)
  # author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "author")

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  commenter = models.ForeignKey(Profile,  on_delete=models.CASCADE, related_name= "commenter")
  content = models.TextField()

  def __str__(self):
    return self.content


"""
class Image(models.Model):
  image_name

class Color(models.Model):
  color_code

class Sketch(models.Model):


class DailyColor(models.Model):
  date
  color_code
"""