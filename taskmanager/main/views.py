from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение формы в базу данных
            return redirect('home')  # Перенаправление на главную страницу после успешного добавления
    else:
        form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
