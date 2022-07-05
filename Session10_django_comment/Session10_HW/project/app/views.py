from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.
def home(request):
    posts = Post.objects.all()
  
    return render(request, 'app/home.html', {"posts": posts})

def detail_post(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  
  post.counting += 1 
  post.save()

  if request.method =='POST':
    new_comment = Comment.objects.create(
      post = post,
      content = request.POST['content']
    )
    return redirect('detail_post', post_pk) 

  return render(request, 'app/detail_post.html', {"post": post, "counting": post.counting})


def create_post(request):
  if request.method =='POST':
    new_post = Post.objects.create(
      title = request.POST['title'],
      content = request.POST['content']
    )
    return redirect('detail_post', new_post.pk)
  return render(request, 'app/create_post.html')

def edit_post(request, post_pk):
  post = Post.objects.filter(pk=post_pk)
  if request.method =='POST':
    post.update(
      title = request.POST['title'],
      content = request.POST['content']
    )
    return redirect('detail_post', post_pk)
  return render(request, 'app/edit_post.html', {'post': post[0]})

def delete_post(request, post_pk):
  post = Post.objects.filter(pk=post_pk)
  post.delete()
  return redirect('home')

def delete_comment(request, post_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('detail_post', post_pk)
