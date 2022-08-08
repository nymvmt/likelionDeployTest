from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateformat import DateFormat

    
# Create your views here.
def home(request):
  today = DateFormat(datetime.now()).format('Y/m/d')
  
  if request.method =='POST':
      new_post = Post.objects.create(
        title=request.POST['title'],
        content=request.POST['content'],
        image = request.POST['image'],
      )
      return redirect('detail', new_post.pk)
  return render(request, 'blog/home.html', {'today':today})


def mypage(request):
  posts = Post.objects.all()
  return render(request, 'blog/mypage.html', {'posts':posts})
        

def detail(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  return render(request, 'blog/detail.html',{'post': post})