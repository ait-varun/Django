import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = []

class NewTaskForm(forms.Form):
  task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html",{
      "newyear": now.month == 1 and now.day == 1,
      "tasks": tasks
    })

def add(request):
  if request.method == "POST":
    form = NewTaskForm(request.POST)
    if form.is_valid():
      task = form.cleaned_data["task"]
      tasks.append(task)
      return HttpResponseRedirect(reverse("index"))
    else:
      return render(request, "newyear/add.html",{"form": form})
  return render(request, "newyear/add.html",{"form": NewTaskForm()})