from django.shortcuts import render
from todo_app.models import Task

def home(request):
	tasks = Task.objects.filter(is_completed = False)
	# print(tasks)
	context = {
	   'mess': tasks
	}
	return render(request, 'home.html', context)