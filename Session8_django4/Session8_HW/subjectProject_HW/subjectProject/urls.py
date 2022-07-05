"""subjectProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from subjectApp import views
from subjectApp.views import AddMajorView, AddSubjectView, EditSubjectView, DeleteSubjectView, EditMajorView, DeleteMajorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addMajor/', AddMajorView.as_view(), name="addMajor"),
    path('', views.home, name='home'),
    #as_view()는 url 해석기에서 class view로 진입하기 위한 매소드;
    path('addSubject/', AddSubjectView.as_view(), name="addSubject"), #class는 as_view 메소드를 넘겨줘야 하는데,
    path('computer/', views.computerSubjectView, name="computer"), #함수는 함수 그 자체를 넘겨줘야함. 그래서 뒤에 .as_View()쓰면 안 됨. 오류남.
    path('editSubject/<int:pk>', EditSubjectView.as_view(), name="editSubject"),
    path('deleteSubject/<int:subject_pk>', DeleteSubjectView, name="deleteSubject"),
    path('editMajor/<int:pk>', EditMajorView.as_view(), name="editMajor"),
    path('deleteMajor/<int:major_pk>', DeleteMajorView, name="deleteMajor"),
]
