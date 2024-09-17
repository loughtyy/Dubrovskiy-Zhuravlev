from .forms import UserForm
from django.shortcuts import render
from django.http import *

def index(request):
 if request.method == "POST":
  name = request.POST.get("name") # получить значения поля Имя
  age = request.POST.get("age") # значения поля Возраст
  output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
  return HttpResponse(output)
 else:
   userform = UserForm()
   return render(request, "app/index.html", {"form": userform})


def about(request):
 return HttpResponse("About")
def contact(request):
 return HttpResponseRedirect("/about")
def details(request):
 return HttpResponsePermanentRedirect("/")
def products(request, productid = 1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(request,id=1, name='Максим'):
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} </h3> ".format(id,name)
    return HttpResponse(output)

