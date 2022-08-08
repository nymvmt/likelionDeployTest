from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User, Profile

# Create your views here.
def signup(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password=request.POST['password1']
        found_user = User.objects.filter(username=username)

        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, 'accounts/signup.html', {"error": error})

        if request.POST['password1'] != request.POST['password2']:
            error = "비밀번호가 다릅니다."
            return render(request, 'accounts/signup.html', {"error": error})
        
        new_user = User.objects.create_user(username = username, password=password,) 
        auth.login(request, new_user) #회원가입하면 바로 로그인되도록 하기.
        return redirect("home")
    return render(request, 'accounts/signup.html')
        

def login(request):
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장하기.
        username = request.POST['username']
        password = request.POST['password']
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, not none이니까 존재한다면!)
        if user is not None:
            auth.login(request, user) #세션에 로그인 정보를 생성 & 저장 -> 페이지 이동 시에도 로그인이 유지되도록 함.
            return redirect('home')
        error = 'ID나 Password가 틀립니다.'
        return render(request, 'accounts/login.html', {'error': error})

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)

    return redirect('home')

# def main(request):
#   return render(request, 'accounts/main.html')