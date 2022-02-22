from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import category,product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
# def index(request):
#     return HttpResponse("hello pillu")



def allproduct(request,category_slug=None):
    category_page=None
    Products_list=None
    if category_slug!=None:
        category_page=get_object_or_404(category,slug=category_slug)
        Products_list=product.objects.all().filter(Category=category_page,available=True)
    else:
        Products_list=product.objects.all().filter(available=True)
    paginator=Paginator(Products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        Products=paginator.page(page)
    except( EmptyPage,InvalidPage):
        Products=paginator.page(paginator.num_pages)

    return render(request,"Category.html",{'Category':category_page,'Products':Products})

def product_detail(request,cat_slug,pro_slug):
    try:
        Product=product.objects.get(Category__slug=cat_slug,slug=pro_slug)

    except Exception as e:
        raise e
    return  render(request,'product.html',{'Product':Product})
