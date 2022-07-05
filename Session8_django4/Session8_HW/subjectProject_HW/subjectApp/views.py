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

def computerSubjectView(request):
    subjects = Subject.objects.all()
    computer_major = Major.objects.get(name = '컴퓨터학과')
    com_major = subjects.filter(subject_major=computer_major) 

    return render(request, 'computer.html', {'com_major': com_major})



class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')



class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')



def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')