from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all()
  
    return render(request, 'home.html', {"posts": posts})


@login_required(login_url="/registeration/login")
def detail_post(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  post_author = post.author

  post.counting += 1 
  post.save()

  if request.method == "POST":
    content = request.POST["content"]
    Comment.objects.create(post=post, content=content, author=request.user)

    return redirect('detail_post', post_pk) 

  return render(request, 'detail_post.html', {"post": post, "counting": post.counting, "post_author":post_author})


@login_required(login_url="/registeration/login")
def create_post(request):
  if request.method =='POST':
    title = request.POST['title']
    content = request.POST['content']
    new_post = Post.objects.create(title=title, content=content, author=request.user)
    return redirect('detail_post', new_post.pk)

  return render(request, 'create_post.html')


def edit_post(request, post_pk):
  post = Post.objects.filter(pk=post_pk)
  if request.method =='POST':
    post.update(
      title = request.POST['title'],
      content = request.POST['content']
    )
    return redirect('detail_post', post_pk)
  return render(request, 'edit_post.html', {'post': post[0]})


def delete_post(request, post_pk):
  post = Post.objects.filter(pk=post_pk)
  post.delete()
  return redirect('home')


def delete_comment(request, post_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('detail_post', post_pk)



def signup(request):
  if request.method=="POST":
    username = request.POST["username"]
    password = request.POST["password"]

    found_user = User.objects.filter(username=username)
    if len(found_user):
      error="이미 아이디가 존재합니다"
      return render(request, "registration/signup.html", {"error": error})
    
    new_user = User.objects.create_user(username=username, password=password)
    auth.login(request, new_user) 

    return redirect("home")
  return render(request, "registration/signup.html")

def login(request):
  if request.method =="POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(
        request, 
        user, 
        backend="django.contrib.auth.backends.ModelBackend" 
      ) 

      return redirect(request.GET.get("next", "/")) 

    error ="아이디 또는 비밀번호가 틀립니다"
    return render(request, "registration/login.html", {"error":error})
  
  return render(request, "registration/login.html")


def logout(request):
  auth.logout(request)
  return redirect("home")