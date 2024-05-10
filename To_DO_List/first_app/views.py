from django.shortcuts import render
from first_app.models import TaskModel
from first_app.forms import TaskMoelForm
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request,'base.html')


class TaskAdd(CreateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskMoelForm
    context_object_name = 'addlist'
    success_url = reverse_lazy('show_task')
    
class ShowTask(ListView):
    model = TaskModel
    template_name = 'show_task.html'
    context_object_name = 'data'