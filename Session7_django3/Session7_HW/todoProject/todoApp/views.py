from tkinter.tix import DisplayStyle
from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.
def home(request):
    todolists = Todo.objects.all().order_by('Todo_due')
    for i in todolists:
        d_day = i.Todo_due - datetime.date(datetime.now())
        i.remain = d_day.days
    return render(request, 'home.html', {'todolists': todolists})


def detail(request, detail_pk):
    x = Todo.objects.get(pk=detail_pk)   #detailpage라는 이름으로 이 x를 부를 거임.
    todotitle = Todo.objects.get(pk = detail_pk)#.Todo_title
    tododetail = Todo.objects.get(pk = detail_pk).Todo_detail
    tododate = Todo.objects.get(pk = detail_pk).Todo_due

    return render(request, 'detail.html', {'detailpage': x, 'todotitle': todotitle, 'tododetail': tododetail, 'tododate': tododate})

def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            Todo_title = request.POST['title'],
            Todo_detail = request.POST['content'],
            Todo_due = request.POST['duedate']
        )    
        return redirect('detail', new_todo.pk)
    
    return render(request, 'new.html')

def edit(request, detail_pk):
    todo = Todo.objects.get(pk=detail_pk)
    
    if request.method == 'POST':
        edit_todo = Todo.objects.filter(pk=detail_pk).update(
            Todo_title = request.POST['title'],
            Todo_detail = request.POST['detail'], #POST['여기에 들어가는 것은'] edit.html의 input/textarea의 name, label, id
            Todo_due = request.POST['duedate'],
        )
        return redirect('detail', detail_pk)

    return render(request, 'edit.html', {'todo': todo})

def delete(request, detail_pk):
    todo = Todo.objects.get(pk=detail_pk)
    todo.delete()

    return redirect('home')

