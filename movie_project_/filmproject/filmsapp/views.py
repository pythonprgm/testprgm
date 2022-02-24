from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import film
from . forms import Movieform


def key(request):
    Film=film.objects.all()
    context={
        'film_list':Film
    }
    return render(request,'key.html',context)
def details(request, film_id):
    Film=film.objects.get(id=film_id)
    return render(request,"details.html",{'film':Film})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img' ]
        movie=film(name=name,desc=desc,year=year,img=img)
        movie.save()

    return render(request,'add.html')
def update(request,id):
    movie=film.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie=film.objects.get(id=id)
        movie.delete()
        return  redirect('/')
    return render(request,'delete.html')