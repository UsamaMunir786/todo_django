from django.shortcuts import render
from todo_app.models import Task

def home(request):
	tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
	# print(tasks)
	compleated_task = Task.objects.filter(is_completed = True)
	print(compleated_task)
	context = {
	   'mess': tasks,
	   'compleated_task': compleated_task
	}
	return render(request, 'home.html', context)