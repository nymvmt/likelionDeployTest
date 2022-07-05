from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from subjectApp.forms import MajorModelForm, SubjectModelForm
from subjectApp.models import Major, Subject

# Create your views here.
def home(request):
    major = Major.objects.all()
    subject = Subject.objects.all()

    return render(request, 'home.html', {'Major': major, 'Subject': subject})

# 전공 추가
class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

# 과목 추가
class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

# 전공 리스트
def majorListView(request):
    list_major = Major.objects.all()
    return render(request, 'listMajor.html', {'list_major': list_major})

# 전공 수정
class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')

# 전공 삭제
def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')



# 과목 리스트
def subjectListView(request):
    list_subject = Subject.objects.all()
    return render(request, 'listSubject.html', {'list_subject': list_subject})


# 과목 수정
class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

# 과목 삭제
def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')


# 컴퓨터 전공 과목만 보기
def computerSubjectView(request):
    subjects = Subject.objects.all()
    computer_major = Major.objects.get(name = '컴퓨터학과')
    com_major = subjects.filter(subject_major=computer_major) 

    return render(request, 'computer.html', {'com_major': com_major})

