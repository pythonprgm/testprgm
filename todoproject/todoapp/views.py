from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class taskview(ListView):
    model=task
    template_name ='index.html'
    context_object_name = 'Task1'

class taskdetailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'Task'

class taskupdateview(UpdateView):
    model = task
    template_name = 'edit.html'
    context_object_name = 'Task2'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('classveiw')








# Create your views here.
def add(request):
    Task1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date','')
        Task=task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,"index.html",{'Task1':Task1})

# def details(request):
#
#     return render(request,'details.html',)

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method =='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task1=task.objects.get(id=id)
    form=todoform(request.POST or None,instance=Task1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'Task1':Task1})