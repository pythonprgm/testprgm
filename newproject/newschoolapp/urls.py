from . import views
from django.urls import path


urlpatterns = [
    path('', views.demo, name='demo'),
    # path('',views.demo1, name='demo1'),
    # path('add/',views.addition,name='addition'),
    # path('contact/', views.contact, name='contact'),
    # path('detail/', views.detail, name='detail'),
    # path('thanks/',views.thanks,name='thanks'),

]
