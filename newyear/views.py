import datetime
from django.shortcuts import render

tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6", "Task 7", "Task 8", "Task 9", "Task 10"]

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html",{
      "newyear": now.month == 1 and now.day == 1,
      "tasks": tasks
    })