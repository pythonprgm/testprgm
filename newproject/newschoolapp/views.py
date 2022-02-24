from django.shortcuts import render
from .models import place
from .models import team


#Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'result1': obj1})



# def demo1(request):
#
#     return render(request, "index.html", {'result1': obj1})


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res= x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,"about.html",{'result':res,'result1':res1,'result2':res2,'result3':res3,})

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("we are here to help you")
#
# def detail(request):
#     return render(request,"detail.html")
#
# def thanks(request):
#     return HttpResponse("Thankyou for your response")

