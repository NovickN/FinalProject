from django.shortcuts import render, get_object_or_404
from .models import Todo, Suggestions
from django.urls import reverse_lazy
from .forms import TodoForm, SuggestionForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'todo/index.html')

def todo(request):
    todo_list=Todo.objects.all()
    return render(request, 'todo/todolist.html', {'todo_list': todo_list})

def suggestion(request):
    suggestion_list=Suggestions.objects.all()
    return render(request, 'todo/suggestion.html', {'suggestion_list': suggestion_list})

# Detailed views below

def todolistdetail(request, id):
    todo=get_object_or_404(Todo, pk=id)
    return render(request, 'todo/todolistdetail.html', {'todo': todo})  

def suggestiondetail(request, id):
    suggestion=get_object_or_404(Suggestions, pk=id)
    return render(request, 'todo/suggestiondetail.html', {'suggestion': suggestion})

# Forms start here
@login_required
def newtodolist(request):
    form=TodoForm

    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TodoForm
    else:
        form=TodoForm()
    return render(request, 'todo/newtodolist.html', {'form': form})    

@login_required
def newsuggestion(request):
    form=SuggestionForm

    if request.method=='POST':
        form=SuggestionForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=SuggestionForm
    else:
        form=SuggestionForm()
    return render(request, 'todo/newsuggestion.html', {'form': form})

def loginmessage(request):
    return render(request, 'todo/loginmessage.html')

def logoutmessage(request):
    return render(request, 'todo/logoutmessage.html')
