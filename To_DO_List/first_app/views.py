from django.shortcuts import render,redirect
from first_app.models import TaskModel
from first_app.forms import TaskMoelForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,TemplateView
from django.urls import reverse_lazy
from django.urls import reverse
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
    

    

class TaskUpdate(UpdateView):
    form_class = TaskMoelForm
    model = TaskModel
    template_name = 'edit_task.html'
    success_url = reverse_lazy('show_task')
    
class DeleteTask(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    success_url = reverse_lazy('show_task')
    
class CompletedTask(TemplateView):
    template_name = 'completed_task.html'

    def get_context_data(self, **kwargs):
        task_id = self.request.GET.get('task_id')
        if task_id:
            task = TaskModel.objects.get(pk=task_id)
            task.completed = True
            task.save()
        return super().get_context_data(**kwargs)
    